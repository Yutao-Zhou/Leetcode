class SeatManager:
    #### heapq ####
    def __init__(self, n: int):
        self.unreserved = []
        self.current = 1

    def reserve(self) -> int:
        if self.unreserved:
            return heapq.heappop(self.unreserved)
        else:
            self.current += 1
            return self.current - 1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)