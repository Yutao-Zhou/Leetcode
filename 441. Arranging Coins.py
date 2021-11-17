class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        k = 0
        while 1:
            i += 1
            k += i
            if k >= n:
                return i - 1