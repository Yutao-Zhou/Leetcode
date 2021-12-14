class Solution:
    def isPalindrome(self, s: str) -> bool:
        ##### transform string and compare ######
        # s = list(s)
        # i = 0
        # while i < len(s):
        #     if ord(s[i]) < 91 and 64 < ord(s[i]):
        #         s[i] = chr(ord(s[i]) + 32)
        #     if ord(s[i]) < 123 and 96 < ord(s[i]) or ord(s[i]) < 58 and 47 < ord(s[i]):
        #         pass
        #     else:
        #         s.pop(i)
        #         i -= 1
        #     i += 1
        # return s == s[::-1]
        
        ##### two pointer ####
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i < j:
            if ord(s[i]) < 48 or ord(s[i]) > 57 and ord(s[i]) < 65 or ord(s[i]) > 90 and ord(s[i]) < 97 or ord(s[i]) > 123:
                i += 1
            if ord(s[j]) < 48 or ord(s[j]) > 57 and ord(s[j]) < 65 or ord(s[j]) > 90 and ord(s[j]) < 97 or ord(s[j]) > 122:
                j -= 1
            elif ord(s[i]) < 123 and 96 < ord(s[i]) or ord(s[i]) < 58 and 47 < ord(s[i]):
                if ord(s[i]) != ord(s[j]):
                    return False
                else:
                    i += 1
                    j -= 1
        return True