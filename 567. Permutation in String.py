class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #### Sliding window ####
        # need, hit, target, l2, i = {}, 0, 0, len(s2), 0
        # for c in s1:
        #     target += 1
        #     if c in need:
        #         need[c] += 1
        #     else:
        #         need[c] = 1
        # if target > l2:
        #     return False
        # while i < l2:
        #     if hit == target:
        #         return True
        #     if s2[i] in need:
        #         need[s2[i]] -= 1
        #         if need[s2[i]] >= 0:
        #             hit += 1
        #     if i - target >= 0:
        #         if s2[i - target] in need:
        #             need[s2[i - target]] += 1
        #             if need[s2[i - target]] > 0:
        #                 hit -= 1
        #     i += 1
        # return hit == target
        
        #### Brute Force Sort ####
        l1, l2 = len(s1), len(s2)
        target = sorted(list(s1))
        for i in range(l1 - 1, l2):
            if sorted(list(s2[i - l1 + 1 : i + 1])) == target:
                return True
        return False