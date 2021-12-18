class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        #### get letters out and put them back in ####
        # letters = []
        # j = -1
        # for string in s:
        #     if 65 <= ord(string) <= 90 or 97 <= ord(string) <= 122:
        #         letters.append(string)
        # ans = list(s)
        # for i in range(len(ans)):
        #     if 65 <= ord(ans[i]) <= 90 or 97 <= ord(ans[i]) <= 122:
        #         ans[i] = letters[j]
        #         j -= 1
        # return "".join(ans)
        
        #### two pointer ####
        s = list(s)
        i = 0 
        j = len(s) - 1
        while i < j:
            if 65 > ord(s[i]) or 97 > ord(s[i]) > 90 or ord(s[i]) > 122:
                i += 1
            elif 65 > ord(s[j]) or 97 > ord(s[j]) > 90 or ord(s[j]) > 122:
                j -= 1
            else:
                s[i],s[j] = s[j],s[i]
                i += 1
                j -= 1 
        return "".join(s)