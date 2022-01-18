class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #### inorder search ####
        i = 0
        ans = strs[0]
        for s in strs:
            if len(s) < len(ans):
                ans = s
        for word in strs:
            i = 0
            while i < len(ans):
                if ans == "":
                    return ans
                elif word[i] != ans[i]:
                    ans = ans[:i]
                i += 1
        return ans