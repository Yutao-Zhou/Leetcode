class Solution:
    def partitionString(self, s: str) -> int:
        #### Greedy ####
        ans, seen = 1, set()
        for c in s:
            if c in seen:
                ans += 1
                seen = set()
            seen.add(c)
        return ans