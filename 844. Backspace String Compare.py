class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #### process both and compare not inplace####
        ps = []
        pt = []
        for i in range(0,len(s)):
            if s[i] == "#" and ps != []:
                ps.pop()
            elif s[i] != "#":
                ps.append(s[i])
        for i in range(0,len(t)):
            if t[i] == "#" and pt != []:
                pt.pop()
            elif t[i] != "#":
                pt.append(t[i])
        return ps == pt