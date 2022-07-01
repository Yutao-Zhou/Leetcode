class Solution:
    def minSwaps(self, s: str) -> int:
        opening, ans = 0, 0
        for b in s:
            if b == "[":
                opening += 1
            else:
                opening -= 1
            ans = min(opening, ans)
        return (-ans + 1) // 2