class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        counter = 0
        i = 1
        while 1:
            if i >= len(s) - counter:
                break
            if abs(ord(s[i]) - ord(s[i-1])) == 32:
                s.append("0")
                s.append("0")
                s.pop(i)
                s.pop(i-1)
                i = 1
                counter += 2
            else:
                i += 1
        s = s[:(len(s)-counter)]
        return "".join(s)