class Solution:
    def replaceDigits(self, s: str) -> str:
        # d = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        # s = list(s)
        # i = 0
        # j = i + 1
        # k = 0
        # while 1:
        #     if j == len(s) + 1 or j == len(s):
        #         return "".join(s)
        #     else:
        #         k = d.index(s[i])
        #         s[j] = (d[k+int(s[j])])
        #         i += 2
        #         j += 2
        ans = []
        for i in s:
            if i.isdigit():
                ans.append(chr(ord(ans[-1])+int(i)))
            else:
                ans.append(i)
        return "".join(ans)