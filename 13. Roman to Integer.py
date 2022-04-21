class Solution:
    def romanToInt(self, s: str) -> int:
        #### iteritive ####
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = table[s[0]]
        for i in range(1, len(s)):
            ans += table[s[i]]
            if table[s[i]] > table[s[i - 1]]:
                ans -= 2 * table[s[i - 1]]
        return ans