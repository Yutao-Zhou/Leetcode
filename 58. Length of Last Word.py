class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = list(s)
        ans = 0
        s.insert(0," ")
        s.insert(0," ")
        for i in range(-1,-len(s),-1):
            if s[i] != " ":
                ans += 1
            if s[i] == " " and s[i+1] != " ":
                return ans