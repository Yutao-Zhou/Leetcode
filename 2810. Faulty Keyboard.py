class Solution:
    def finalString(self, s: str) -> str:
        #### Brute Force ####
        # ans = ""
        # for c in s:
        #     if c == 'i':
        #         ans  = ans[::-1]
        #     else:
        #         ans = ans + c
        # return ans

        #### Flip ####
        n = len(s)
        i = 0
        while i < n:
            if s[i] == 'i':
                s = s[:i][::-1] + s[i + 1:]
                n -= 1
            else:
                i += 1
        return s