class Solution:
    def makeFancyString(self, s: str) -> str:
        #### append and join ####
        # counter = 1
        # ans = [s[0]]
        # for i in range(1,len(s)):
        #     if s[i] == s[i - 1]:
        #         counter += 1
        #         if counter < 3:
        #             ans.append(s[i])
        #     else:
        #         counter = 1
        #         ans.append(s[i])
        #     i += 1
        # return "".join(ans)
        
        #### one pass splice ####
        i = 0
        while i < len(s) - 2:
            if s[i] == s[i + 1] == s[i + 2]:
                s = s[:i + 2] + s[i + 3:]
            else:
                i += 1
        return s