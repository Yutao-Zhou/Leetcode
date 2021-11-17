class Solution:
    def generateTheString(self, n: int) -> str:
        ans = ""
        if n % 2 == 0:
            ans += "a"
            ans += "b"*(n-1)
        else:
            ans += "a"*n
        return ans