class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for c in s:
            if ord(c) >= 65 and ord(c) <= 90:
                ans += chr(ord(c)+32)
            else:
                ans += c
        return ans