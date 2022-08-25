import os
import sys
import pygame
import random

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from Algorithms.ShortestPathInUnWeightedGraph import Graph

def add_figures(princess_pos):
    i = 0

    # Vẽ hoàng tử
    if not isStart and arr_princeCoord:
        princeIcon_rect = princeIcon.get_rect(topleft=(top_left[0] + 3, top_left[1] + 3))
        screen.blit(princeIcon, princeIcon_rect)

    # Vẽ công chúa
    princessIcon_rect = princessIcon.get_rect(topleft=princess_pos)
    screen.blit(princessIcon, princessIcon_rect)

    # Vẽ các ghost
    for coord in arr_ghostesCoord:
        if arr_randInt[i] == 0:
            fileName = "assets/image/ghostIcon.png"
        else:
            fileName = "assets/image/dragonIcon.png"
        i += 1

        ghostIcon = pygame.image.load(fileName).convert_alpha()
        ghostIcon_rect = ghostIcon.get_rect(topleft=(top_left[0] + (separator * coord[1]) + 2, top_left[1] + (separator * coord[0]) + 2))
        screen.blit(ghostIcon, ghostIcon_rect)

def board_game():
    # trên
    pygame.draw.line(screen, WHITE, top_left, top_right)
    # phải
    pygame.draw.line(screen, WHITE, top_right, bottom_right)
    # dưới
    pygame.draw.line(screen, WHITE, bottom_right, bottom_left)
    # trái
    pygame.draw.line(screen, WHITE, bottom_left, top_left)

    x = top_left[0]
    y = top_left[1]
    for i in range(1, grid):
        x += separator
        y += separator

        # vẽ đường ngang
        pygame.draw.line(screen, WHITE, (top_left[0], y), (top_right[0], y))
        # vẽ đường dọc
        pygame.draw.line(screen, WHITE, (x, top_left[1]), (x, bottom_left[1]))

    add_figures((bottom_right[0] - 32, bottom_right[1] - 30))

def control_panel(mouse_coord):
    title_surface = title_font.render(
        "RESCUE THE PRINCESS", True, (233, 14, 206))
    title_rect = title_surface.get_rect(midright=(750, 70))

    start_borderColor = "assets/image/blueBorder.png"
    start_textColor = (97, 168, 214)
    reset_borderColor = "assets/image/blueBorder.png"
    reset_textColor = (97, 168, 214)

    # khi rê chuột đến button "PRESS START"
    if mouse_coord[0] >= 538 and mouse_coord[0] <= 684 and mouse_coord[1] >= 119 and mouse_coord[1] <= 179:
        start_borderColor = "assets/image/yellowBorder.png"
        start_textColor = (209, 187, 19)
    
    # khi rê chuột đến button "RESET"
    if mouse_coord[0] >= 553 and mouse_coord[0] <= 674 and mouse_coord[1] >= 194 and mouse_coord[1] <= 243:
        reset_borderColor = "assets/image/yellowBorder.png"
        reset_textColor = (209, 187, 19)

    start_border = pygame.image.load(start_borderColor).convert_alpha()
    startBorder_rect = start_border.get_rect(midright=(680, 150))
    startFont_surface = start_font.render("PRESS START", True, start_textColor)
    startFont_rect = startFont_surface.get_rect(midright=(670, 150))

    reset_border = pygame.image.load(reset_borderColor).convert_alpha()
    resetBorder_rect = reset_border.get_rect(midright=(680, 220))
    resetFont_surface = reset_font.render("RESET", True, reset_textColor)
    resetFont_rect = resetFont_surface.get_rect(midright=(640, 220))

    prince_rect = prince.get_rect(bottomright=(700, 480))
    princess_rect = princess.get_rect(bottomright=(780, 380))
    dragon_rect = dragon.get_rect(bottomright=(555, 360))
    ghost_rect = ghost.get_rect(bottomright=(780, 500))

    screen.blit(title_surface, title_rect)
    screen.blit(start_border, startBorder_rect)
    screen.blit(startFont_surface, startFont_rect)
    screen.blit(reset_border, resetBorder_rect)
    screen.blit(resetFont_surface, resetFont_rect)
    screen.blit(princess, princess_rect)
    screen.blit(dragon, dragon_rect)
    screen.blit(prince, prince_rect)
    screen.blit(ghost, ghost_rect)

def setting_ghostesANDprinceCoord():
    while True:
        g = generateGameGraph()

        minChoice_perRow = 0
        maxChoice_perRow = grid - 2
        arr_ghostesIndex = []
        arr_ghostesPos = []
        arr_princePos = []

        for i in range(grid):
            # số lượng index được chọn trên mỗi dòng
            numChoice_perRow = random.randint(minChoice_perRow, maxChoice_perRow)

            # các index nằm trên dòng thứ i
            arrIndex_inRow = [((grid * i) + x) for x in range(grid)]

            while numChoice_perRow > 0:
                # index được chọn trên dòng thứ i
                index_choiced = random.choice(arrIndex_inRow)
                while index_choiced == 0 or index_choiced == ((grid * grid) - 1):
                    index_choiced = random.choice(arrIndex_inRow)

                # Xác định các đỉnh có ghost
                arr_ghostesIndex.append(index_choiced)
                
                # loại bỏ index đã được chọn trên dòng thứ i
                arrIndex_inRow.remove(index_choiced)

                numChoice_perRow -= 1

        # Xóa các cạnh liên kết đến đỉnh có ghost
        for v in arr_ghostesIndex:
            g.removeVertex(v)

        if g.shortestPath(0, ((grid * grid) - 1)) != -1:
            # Mảng tọa độ của mỗi con ghost (dòng thứ i, cột thứ j)
            arr_ghostesPos = [(int(v / grid), v % grid) for v in arr_ghostesIndex]

            # Mảng tọa độ của prince (dòng thứ i, cột thứ j)
            arr_princePos = [(int(v / grid), v % grid) for v in g.shortestPath(0, ((grid * grid) - 1))]

            return [arr_ghostesPos, arr_princePos]

def generateGameGraph():
    g = Graph(grid * grid)

    for r in range(grid):
        for c in range(grid):
            i = (grid * r) + c
            if (c + 1) < grid:
                g.addEdge(i, i + 1)
            if (r + 1) < grid:
                g.addEdge(i, i + grid)

    return g

# Chuyển đổi âm thanh cho pygame dễ xử lí
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)

# Khởi tạo cửa sổ pygame
pygame.init()
screen = pygame.display.set_mode((800, 518))
clock = pygame.time.Clock()

intro_bg = pygame.image.load("assets/image/background.png").convert_alpha()
btn_play = pygame.image.load("assets/image/buttonPlay.png").convert_alpha()
play_sound = pygame.mixer.Sound("assets/sound/play_sound.wav")
reset_sound = pygame.mixer.Sound("assets/sound/reset_sound.wav")
start_sound = pygame.mixer.Sound("assets/sound/start_sound.wav")
title_font = pygame.font.Font("assets/font/BeatWordDemo-nRL20.ttf", 35)
step_font = pygame.font.Font("assets/font/BeatWordDemo-nRL20.ttf", 20)
start_font = pygame.font.Font("assets/font/EvilEmpire-4BBVK.ttf", 25)
reset_font = pygame.font.Font("assets/font/EvilEmpire-4BBVK.ttf", 25)
prince = pygame.image.load("assets/image/prince.png").convert_alpha()
princess = pygame.image.load("assets/image/princess.png").convert_alpha()
dragon = pygame.image.load("assets/image/dragon.png").convert_alpha()
ghost = pygame.image.load("assets/image/ghost.png").convert_alpha()
princeIcon = pygame.image.load("assets/image/princeIcon.png").convert_alpha()
princessIcon = pygame.image.load("assets/image/princessIcon.png").convert_alpha()

WHITE = (255, 255, 255)
FPS = 5 # frames-per-second
isPlay = False
grid = 10
top_left = (50, 120)
top_right = (400, 120)
bottom_left = (50, 470)
bottom_right = (400, 470)
separator = int(round(350 / grid, 0))
arr_ghostesCoord = []
arr_randInt = []
arr_princeCoord = [(0, 0)]
isSuccessfullyBoard = False
isStart = False
endCoord_prince = ()
step = 0

# Tạo vòng lặp cho pygame
while True:

    # Lấy tất cả sự kiện pygame xảy ra
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # thoát game
            sys.exit()  # thoát hệ thống
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Khi nhấn button "PLAY"
            if isPlay == False and mouse[0] >= 564 and mouse[0] <= 726 and mouse[1] >= 277 and mouse[1] <= 353:
                play_sound.play()
                isPlay = True

            # Khi nhấn button "PRESS START"
            if isPlay and isStart == False and mouse[0] >= 538 and mouse[0] <= 684 and mouse[1] >= 119 and mouse[1] <= 179:
                start_sound.play()
                isStart = True

            # Khi nhấn button "RESET"
            if isSuccessfullyBoard and isStart == False and mouse[0] >= 553 and mouse[0] <= 674 and mouse[1] >= 194 and mouse[1] <= 243:
                reset_sound.play()
                step = 0
                isSuccessfullyBoard = False

    # Lưu trữ 1 tuple chứa tọa độ (x, y) của chuột ghi rê vào screen
    mouse = pygame.mouse.get_pos()

    if isPlay:
        screen.fill((32, 23, 86))
        control_panel(mouse)

        if isStart and arr_princeCoord and arr_princeCoord[0] != (0, 0):
            step += 1
        stepFont_surface = step_font.render(f'STEP: {step}', True, (255, 255, 255))
        stepFont_rect = stepFont_surface.get_rect(topleft=(50, 70))
        screen.blit(stepFont_surface, stepFont_rect)

        board_game()
        if isSuccessfullyBoard == False:
            arr_ghostesCoord, arr_princeCoord = setting_ghostesANDprinceCoord()

            for i in range(len(arr_ghostesCoord)):
                arr_randInt.append(random.randint(0, 1))

            isSuccessfullyBoard = True
    else:
        screen.blit(intro_bg, (0, 0))
        if mouse[0] >= 564 and mouse[0] <= 726 and mouse[1] >= 277 and mouse[1] <= 353:
            screen.blit(btn_play, (560, 274))

    if isStart:
        # Vẽ hoàng tử
        if arr_princeCoord:
            princeIcon_rect = princeIcon.get_rect(topleft=(top_left[0] + (separator * arr_princeCoord[0][1]) + 3, top_left[1] + (separator * arr_princeCoord[0][0]) + 3))
            screen.blit(princeIcon, princeIcon_rect)
            endCoord_prince = arr_princeCoord.pop(0)
        else:
            isStart = False
    else:
        if not arr_princeCoord:
            princeIcon_rect = princeIcon.get_rect(topleft=(top_left[0] + (separator * endCoord_prince[1] + 3), top_left[1] + (separator * endCoord_prince[0]) + 3))
            screen.blit(princeIcon, princeIcon_rect)

    # Cập nhật khung hình
    pygame.display.update()

    # Tốc độ khung hình mỗi giây
    clock.tick(FPS)
