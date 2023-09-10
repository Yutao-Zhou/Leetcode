class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        #### Backtrack ####
        def createString(start, path):
            if start == len(s):
                nonlocal ans
                ans = max(ans, len(path))
            for i in range(start + 1, len(s) + 1):
                if s[start : i] not in path:
                    path.add(s[start : i])
                    createString(i, path)
                    path.remove(s[start : i])
        
        ans = 0
        createString(0, set())
        return ans