class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        sum_team = skill[0] + skill[-1]
        n = len(skill)
        ans = 0
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != sum_team:
                return -1
            ans += skill[i] * skill[n - i - 1]
        return ans