class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #### Backtrack ####
        # def find(start):
        #     if start == len(s):
        #         return True
            
        #     for i in range(start + 1, len(s) + 1):
        #         if s[start : i] in wordDict:
        #             if find(i):
        #                 return True
        
        # wordDict = set(wordDict)
        # return find(0)

        #### DP Bottomup ####
        memo = [False] * (len(s) + 1)
        memo[0] = True
        wordDict = set(wordDict)
        for i in range(len(s)):
            if memo[i] == True:
                for j in range(i + 1, len(s) + 1):
                    if s[i : j] in wordDict:
                        memo[j] = memo[i]

        return memo[-1]