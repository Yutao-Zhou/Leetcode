class Solution:
    def countSegments(self, s: str) -> int:
        #### count word two flag ####
        # start, end = False, False
        # ans = 0
        # s += "  "
        # s = " " + s
        # for i in range(len(s) - 1):
        #     if s[i] != " " and s[i - 1] == " ":
        #         start = True
        #     if s[i] == " " and s[i - 1] != " ":
        #         end = True
        #     if start and end:
        #         ans += 1
        #         start, end = False, False
        # return ans
        
        #### fake one liner #####
        # return len(s.split())
        
        #### one pass clasic ####
        ans = 0
        for i in range(len(s)):
            if i == 0 and s[i] != " ":
                ans += 1
            elif s[i - 1] == " " and s[i] != " ":
                ans += 1
        return ans