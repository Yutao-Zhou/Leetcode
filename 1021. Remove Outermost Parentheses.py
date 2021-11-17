class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i = 0
        j = 0
        c = 0
        s = list(s)
        s.append("")
        while 1:
            if s[i] == ")":
                i += 1
            else:
                pass
            if s[j] == "(":
                c += 1
                j += 1
            if s[j] != "(":
                if s[j] == ")" and c == 1:
                    s[j] = ""
                    s[i] = ""
                    c = 0
                    j += 1
                    i = j
                elif s[j] == ")":
                    c -= 1
                    j += 1
            if j == len(s)-1 or i == len(s)-1:
                s = "".join(s)
                return s