class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ans = []
        for i in range(0,len(s),1):
            if s[i] == "":
                s.append(0)
                s.pop(i)
        for i in range(-1, -len(s)-1, -1):
            if s[i] != "" and s[i] != 0:
                ans.append(s[i])
            else:
                s.append(0)
                s.pop(i)
        return " ".join(ans)