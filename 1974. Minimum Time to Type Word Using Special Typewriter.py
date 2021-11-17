class Solution:
    def minTimeToType(self, word: str) -> int:
        cach = "a"
        ans = 0
        for i in word:
            if abs(ord(i) - ord(cach)) > 13:
                ans += 26 - abs(ord(i) - ord(cach))
                cach = i
            else:
                ans += abs(ord(i) - ord(cach))
                cach = i
        return ans + len(word)