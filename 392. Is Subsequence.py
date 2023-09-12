class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #### Two Pointers ####
        if s == '':
            return True
        i, j = 0, 0
        while i < len(s):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j == len(t):
                break
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)