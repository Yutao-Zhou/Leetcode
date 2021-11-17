class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        for i in s:
            if i == "L":
                l += 1
            if i == "R":
                r += 1
            if l == r:
                ans += 1
                l = 0
                r = 0
        return ans