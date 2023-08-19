class ProductOfNumbers:

    def __init__(self):
        self.queue = [1]
        self.len_queue = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.queue = [1]
            self.len_queue = 1
        else:
            self.queue.append(self.queue[-1] * num)
            self.len_queue += 1

    def getProduct(self, k: int) -> int:
        if k >= self.len_queue:
            return 0
        return self.queue[-1] // self.queue[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)