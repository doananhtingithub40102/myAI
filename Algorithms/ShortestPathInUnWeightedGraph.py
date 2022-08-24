"""
Chương trình python
tìm đường đi ngắn nhất giữa 2 đỉnh
    từ đỉnh src (source - nguồn) đến đỉnh dest (destination - đích)
trong đồ thị không trọng số
sử dụng biến thể của BFS
    lưu trữ pre (predecessor - đỉnh trước đó) của đỉnh đang xét
"""

from collections import defaultdict

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from DataStructure.QueueUsingArray import QueueUsingArray

class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def removeVertex(self, vertex):
        self.graph.pop(vertex)
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] == vertex:
                    self.graph[i].pop(j)
                    break

    def BFS(self, src, dest, pre):
        visited = [False for i in range(self.vertex)]
        queue = QueueUsingArray(self.vertex - 1)

        # Thêm src (nút start) vào Queue trước tiên và đánh dấu đã duyệt qua 
        queue.enQueue(src)
        visited[src] = True

        while (not queue.isEmpty()):

            # Xóa phần tử đầu
            src = queue.deQueue()

            for i in self.graph[src]:
                if visited[i] == False:
                    queue.enQueue(i)
                    pre[i] = src
                    visited[i] = True
                    
                    # dừng BFS khi tìm thấy đỉnh đích
                    if i == dest:
                        return True
            
        return False

    def shortestPath(self, src, dest):
        pre = [-1  for i in range(self.vertex)]
        if self.BFS(src, dest, pre):
            path = []
            curr = dest
            while curr != src:
                path.insert(0, curr)
                curr = pre[curr]
            path.insert(0, src)

            return path
        
        return -1

if __name__ == "__main__":
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(3, 4)
    g.addEdge(3, 7)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 6)
    g.addEdge(6, 7)

    print(g.graph)

    # g.removeVertex(1)
    # print(g.graph)
    
    print(g.shortestPath(0, 7))