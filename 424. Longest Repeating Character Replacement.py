class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, i, j, freqMap = 0, 0, 0, [0] * 26
        while j < len(s):
            if sum(freqMap) - max(freqMap) <= k:
                freqMap[ord(s[j]) - 65] += 1
                j += 1
            if sum(freqMap) - max(freqMap) > k:
                freqMap[ord(s[i]) - 65] -= 1
                i += 1
                ans = max(ans, j - i)
        ans = max(ans, j - i)
        return ans