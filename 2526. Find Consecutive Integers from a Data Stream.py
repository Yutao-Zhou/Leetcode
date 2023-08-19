class DataStream:
    #### Simulate with fix length queue ####
    # def __init__(self, value: int, k: int):
    #     self.queue = [0] * k
    #     self.hit = 0
    #     self.value = value
    #     self.k = k
    #     self.pointer = 0

    # def consec(self, num: int) -> bool:
    #     if self.queue[self.pointer] == self.value:
    #         self.hit -= 1
    #     self.queue[self.pointer] = num
    #     self.pointer = (self.pointer + 1) % self.k
    #     if num == self.value:
    #         self.hit += 1
    #     return self.hit == self.k

    #### Count ####
    def __init__(self, value: int, k: int):
        self.hit = 0
        self.k = k
        self.value = value

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.hit += 1
        else:
            self.hit = 0
        return self.hit >= self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)