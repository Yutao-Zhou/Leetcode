class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        #### Simulation ####
        r1, c1, r2, c2 = int(s[1]), ord(s[0]), int(s[4]), ord(s[3])
        ans = []
        for column in range(c1, c2 + 1):
            for row in range(r1, r2 + 1):
                ans.append(f"{chr(column)}{row}")
        return ans