class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        between = False
        for n in s:
            if n == "|":
                between ^= True
            if between == False and n == "*":
                ans += 1
        return ans