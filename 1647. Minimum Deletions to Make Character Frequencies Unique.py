class Solution:
    def minDeletions(self, s: str) -> int:
        #### frequency map and calculate ####
        ans = 0
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            if char not in freq:
                freq[char] = 1
        freq = sorted(freq.values())
        i = len(freq) - 2
        while i >= 0:
            if freq[i] == freq[i + 1] and freq[i] != 0:
                ans += 1
                freq[i] -= 1
                freq = sorted(freq)
            else:
                i -= 1
        return ans