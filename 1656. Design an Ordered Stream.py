class OrderedStream:
    def __init__(self, n: int):
        self.stream = [0] * (n + 1)
        self.counter = 1
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        cache = []
        while self.stream[self.counter] != 0:
            cache.append(self.stream[self.counter])
            self.counter += 1
            if self.counter > self.n:
                break
        return cache
            


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)