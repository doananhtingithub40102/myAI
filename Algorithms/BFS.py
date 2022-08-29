"""
Chương trình python duyệt tìm kiếm BFS (Breadth-First-Search)
"""

from collections import defaultdict

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # Thư mục cha của file BFS.py
sys.path.append(os.path.dirname(SCRIPT_DIR)) # thêm "d:\myAI" vào danh sách đường dẫn

from DataStructure.QueueUsingArray import QueueUsingArray

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = QueueUsingArray(10)

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
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(4, 5)

    g.BFS(0)