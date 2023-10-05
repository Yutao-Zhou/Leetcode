class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = 1 - n & 1
        while n:
            if n & 1 == last:
                return False
            last ^= 1
            n >>= 1
        return True