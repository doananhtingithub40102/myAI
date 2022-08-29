"""
Chương trình python sử dụng array để triển khai Stack
"""

# Class StackUsingArray đại diện 1 Stack
class StackUsingArray:
    def __init__(self, capacity):
        self.S = []
        self.capacity = capacity

    def isFull(self):
        return len(self.S) == self.capacity

    def isEmpty(self):
        return len(self.S) == 0

    def enStack(self, item):
        if (not self.isFull()):
            self.S.insert(0, item)

    def deStack(self):
        if (not self.isEmpty()):
            return self.S.pop(0)

    def getHead(self):
        if (not self.isEmpty()):
            return self.S[0]
        return None

    def getTail(self):
        if (not self.isEmpty()):
            return self.S[len(self.S) - 1]
        return None

if __name__ == "__main__":
    queue = StackUsingArray(5)
    queue.enStack(10)
    queue.enStack(20)
    queue.enStack(30)
    queue.enStack(40)
    queue.deStack()
    print(queue.S)
    print(queue.getHead())
    print(queue.getTail())