class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #### Hash Table Sliding Window ####
        # sl, pl = len(s), len(p)
        # if sl < pl:
        #     return []
        # pointer = pl
        # ans, window, pMap = [], [0] * 26, [0] * 26
        # for i in range(len(p)):
        #     pMap[ord(p[i]) - 97] += 1
        #     window[ord(s[i]) - 97] += 1
        # while pointer < sl:
        #     if window == pMap:
        #         ans.append(pointer - pl)
        #     window[ord(s[pointer]) - 97] += 1
        #     window[ord(s[pointer - pl]) - 97] -= 1
        #     pointer += 1
        # if window == pMap:
        #     ans.append(pointer - pl)
        # return ans
        
        #### Brute Force very very slow ####
        ans = []
        p = sorted(list(p))
        pl = len(p)
        for i in range(len(s) - pl + 1):
            if sorted(list(s[i : i + pl])) == p:
                ans.append(i)
        return ans