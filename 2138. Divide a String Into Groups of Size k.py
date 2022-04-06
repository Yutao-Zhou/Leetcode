class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        #### simulation ####
        ans = []
        while s:
            if len(s) > k:
                ans.append(s[:k])
                s = s[k:]
            else:
                ans.append(s + fill * (k - len(s)))
                break
        return ans