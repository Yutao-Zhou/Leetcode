class StockSpanner:
    #### Jump Loop ####
#     def __init__(self):
#         self.historyPrice = []
#         self.historySpan = []
#         self.lenPrice = 0

#     def next(self, price: int) -> int:
#         i = -1
#         if self.historyPrice and self.historyPrice[-1] < price:
#             i = min(i, -self.historySpan[-1])
#         span = -i
#         while -i <= self.lenPrice and self.historyPrice[i] <= price:
#             span += self.historySpan[i]
#             i -= self.historySpan[i]
#         self.historyPrice.append(price)
#         self.lenPrice += 1
#         self.historySpan.append(span)
#         return span

    #### Stack ####
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)