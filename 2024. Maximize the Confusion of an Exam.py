class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #### Sliding window ####
        ans = 0
        l, r = 0, 0
        n = len(answerKey)
        current = {"T": 0, "F": 0}
        while l < n and r < n:
            current[answerKey[r]] += 1
            if current["T"] > k and current["F"] > k:
                current[answerKey[l]] -= 1
                l += 1
                r += 1
            else:
                ans = max(ans, r - l + 1)
                r += 1
        return ans