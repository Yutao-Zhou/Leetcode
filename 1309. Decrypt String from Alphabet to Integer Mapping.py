class Solution:
    def freqAlphabets(self, s: str) -> str:
        s = list(s)
        cach = 0
        i = -1
        while 1:
            if i == -len(s) - 1:
                return "".join(s)
            if s[i] == "#":
                s[i] = ""
                cach = int(s[i-1]) + int(s[i-2]) * 10
                s[i-1] = chr(cach + 96)
                s[i-2] = ""
                i -= 1
            try:
                cach = int(s[i])
                s[i] = chr(cach + 96)
                i -= 1
            except:
                TypeError
                i -= 2