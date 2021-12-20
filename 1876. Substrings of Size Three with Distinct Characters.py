class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        #### hard solve no skill ####
        # ans = 0
        # for i in range(2,len(s)):
        #     if s[i] != s[i - 1] and s[i] != s[i - 2] and s[i - 1] != s[i - 2]:
        #         ans += 1
        # return ans
        
        #### same idea but using set ####
        ans = 0
        for i in range(2,len(s)):
            if len(set(s[i - 2:i + 1])) == 3:
                ans += 1
        return ans