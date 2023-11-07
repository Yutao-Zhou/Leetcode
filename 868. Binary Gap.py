class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        counter = 1
        one = False
        while n:
            if not(n & 1) and one:
                counter += 1
            elif n & 1:
                if one:
                    ans = max(ans, counter)
                    counter = 1
                one = True
            n >>= 1
        return ans