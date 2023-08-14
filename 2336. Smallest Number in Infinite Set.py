class SmallestInfiniteSet:
    #### heapq ####
    # def __init__(self):
    #     self.current = 1
    #     self.heap = []

    # def popSmallest(self) -> int:
    #     if self.heap:
    #         return heapq.heappop(self.heap)
    #     self.current += 1
    #     return self.current - 1

    # def addBack(self, num: int) -> None:
    #     if self.current > num and num not in self.heap:
    #         heapq.heappush(self.heap, num)

    #### set ####
    def __init__(self):
        self.added = set()
        self.current = 1

    def popSmallest(self) -> int:
        if self.added:
            smallest = min(self.added)
            self.added.remove(smallest)
            return smallest
        self.current += 1
        return self.current - 1

    def addBack(self, num: int) -> None:
        if self.current > num:
            self.added.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)