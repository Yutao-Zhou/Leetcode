class Solution:
    def validPalindrome(self, s: str) -> bool:
        #### two pointer ####
        i = 0
        j = len(s) - 1
        def check(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        while i < j:
            if s[i] != s[j]:
                return check(s, i, j - 1) or check(s, i + 1, j)
            i += 1
            j -= 1
        return True