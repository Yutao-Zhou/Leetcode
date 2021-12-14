class Solution:
    def maxPower(self, s: str) -> int:
        counter =1
        ans = 1
        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                counter += 1
                if counter > ans:
                    ans = counter
            else:
                counter = 1
        return ans