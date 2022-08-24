"""
Chương trình python duyệt tìm kiếm BFS (Breadth-First-Search)
"""

from collections import defaultdict

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # Thư mục cha của file BFS.py
sys.path.append(os.path.dirname(SCRIPT_DIR)) # thêm "d:\AI" vào danh sách đường dẫn

from DataStructure.QueueUsingArray import QueueUsingArray

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = QueueUsingArray(max(self.graph))

        # Thêm s (nút start) vào Queue trước tiên và đánh dấu đã duyệt qua 
        queue.enQueue(s)
        visited[s] = True

        while (not queue.isEmpty()):

            # Xóa phần tử đầu và in nó
            s = queue.deQueue()
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.enQueue(i)
                    visited[i] = True

if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 11)
    g.addEdge(2, 1)
    g.addEdge(2, 4)
    g.addEdge(2, 6)
    g.addEdge(3, 1)
    g.addEdge(3, 4)
    g.addEdge(4, 2)
    g.addEdge(4, 3)
    g.addEdge(4, 6)
    g.addEdge(5, 9)
    g.addEdge(5, 10)
    g.addEdge(6, 2)
    g.addEdge(6, 4)
    g.addEdge(6, 7)
    g.addEdge(6, 8)
    g.addEdge(7, 6)
    g.addEdge(8, 6)
    g.addEdge(8, 10)
    g.addEdge(9, 5)
    g.addEdge(9, 13)
    g.addEdge(10, 5)
    g.addEdge(10, 8)
    g.addEdge(11, 1)
    g.addEdge(11, 12)
    g.addEdge(11, 13)
    g.addEdge(12, 11)
    g.addEdge(12, 13)
    g.addEdge(13, 9)
    g.addEdge(13, 11)
    g.addEdge(13, 12)

    g.BFS(1)