"""
Chương trình python sử dụng array để triển khai Queue
"""

# Class QueueUsingArray đại diện 1 Queue
class QueueUsingArray:
    def __init__(self, capacity):
        self.Q = []
        self.capacity = capacity

    def isFull(self):
        return len(self.Q) == self.capacity

    def isEmpty(self):
        return len(self.Q) == 0

    def enQueue(self, item):
        if (not self.isFull()):
            self.Q.append(item)

    def deQueue(self):
        if (not self.isEmpty()):
            return self.Q.pop(0)

    def getFront(self):
        if (not self.isEmpty()):
            return self.Q[0]
        return None

    def getRear(self):
        if (not self.isEmpty()):
            return self.Q[len(self.Q) - 1]
        return None

if __name__ == "__main__":
    queue = QueueUsingArray(5)
    queue.enQueue(10)
    queue.enQueue(20)
    queue.enQueue(30)
    queue.enQueue(40)
    queue.deQueue()
    print(queue.Q)
    print(queue.getFront())
    print(queue.getRear())