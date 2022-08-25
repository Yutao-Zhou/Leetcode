class Solution:
    def repeatedCharacter(self, s: str) -> str:
        #### Count and return ####
        seen = set()
        for c in s:
            if c in seen:
                return c
            if c not in seen:
                seen.add(c)