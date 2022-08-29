"""
Chương trình python duyệt tìm kiếm DFS (Depth-First-Search)
"""

from collections import defaultdict

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # Thư mục cha của file DFS.py
sys.path.append(os.path.dirname(SCRIPT_DIR)) # thêm "d:\AI" vào danh sách đường dẫn

from DataStructure.StackUsingArray import StackUsingArray

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, start):
        visited = [False] * (max(self.graph) + 1)
        stack = StackUsingArray(10)

        # Thêm start vào Stack trước tiên và đánh dấu đã duyệt qua 
        stack.enStack(start)
        visited[start] = True

        while (not stack.isEmpty()):

            # Xóa phần tử đầu và in nó
            start = stack.deStack()
            print(start, end=" ")

            i = len(self.graph[start]) - 1
            while i >= 0:
                if visited[self.graph[start][i]] == False:
                    stack.enStack(self.graph[start][i])
                    visited[self.graph[start][i]] = True
                i -= 1

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    g.addEdge(5, 7)
    g.addEdge(7, 8)
    g.addEdge(8, 9)
    g.addEdge(8, 10)

    g.DFS(0)