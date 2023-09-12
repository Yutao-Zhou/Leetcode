class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #### Backtrack ####
        def find(start, path):
            if start == len(s):
                nonlocal ans
                ans.append(path[1:])
                return
            
            for i in range(start + 1, len(s) + 1):
                if s[start : i] in wordDict:
                    find(i, path + ' ' + s[start : i])
        
        ans = []
        wordDict = set(wordDict)
        find(0, "")
        return ans