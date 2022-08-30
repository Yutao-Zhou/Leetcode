class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        #### Brute Force Try Every Single Potential One ####
        # l = len(s)
        # for i in range(1, l // 2 + 1):
        #     if l % i == 0:
        #         if s[:i] * (l // i) == s:
        #             return True
        # return False
        
        #### Folding ####
        return s in s[1:] + s[:-1]