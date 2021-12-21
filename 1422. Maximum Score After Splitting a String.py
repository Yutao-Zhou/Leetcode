class Solution:
    def maxScore(self, s: str) -> int:
        #### hard solve ####
        # ans = []
        # cache = 0
        # for i in range(1,len(s)):
        #     for j in s[:i]:
        #         if j == "0":
        #             cache += 1
        #     for j in s[i:]:
        #         if j == "1":
        #             cache += 1
        #     ans.append(cache)
        #     cache = 0
        # return max(ans)
        
        #### count number of one and calculate score ####
        ans = []
        zeros = s.count("0")
        currentZero = 0
        length = len(s)
        for i in range(0,length):
            if s[i] == "0":
                currentZero += 1
            score = 2 * currentZero + length - i - 1 - zeros
            ans.append(score)
        return max(ans[:-1])