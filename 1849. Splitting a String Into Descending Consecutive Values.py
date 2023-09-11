class Solution:
    def splitString(self, s: str) -> bool:
        #### Backtrack ####
        def splitWord(start, last):
            print(start, last)
            if start == len(s):
                nonlocal ans
                ans = True
                return True
            
            for i in range(start + 1, len(s) + 1):
                if int(s[start : i]) + 1 == last:
                    if splitWord(i, int(s[start : i])):
                        return True
        
        ans = False
        for i in range(1, len(s)):
            splitWord(i, int(s[:i]))
        return ans