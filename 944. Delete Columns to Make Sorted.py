class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        i = 0
        ans = 0
        while i < len(strs[0]):
            for j in range(1,len(strs)):
                if ord(strs[j][i]) < ord(strs[j - 1][i]):
                    ans += 1
                    break
            i += 1
        return ans