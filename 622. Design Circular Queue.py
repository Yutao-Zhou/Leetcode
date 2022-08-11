class MyCircularQueue:
    def __init__(self, k: int):
        self.myque = [-1] * k
        self.i, self.j = 0, float('-inf')
        self.k = k
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.j = self.i + 1
        else:
            self.j += 1
        self.myque[(self.j - 1) % self.k ] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.i += 1
        if self.i % self.k == self.j % self.k:
            self.j = float('-inf')
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.myque[self.i % self.k]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.myque[(self.j - 1) % self.k]
        return -1

    def isEmpty(self) -> bool:
        return self.j == float('-inf')

    def isFull(self) -> bool:
        return self.i % self.k == self.j % self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()