class Solution:
    def minSteps(self, s: str, t: str) -> int:
        #### Sort ####
        # ans = 0
        # s = list(s)
        # s.sort()
        # t = list(t)
        # t.sort()
        # i, j = 0, 0
        # lenS, lenT = len(s), len(t)
        # while i < lenS and j < lenT:
        #     if ord(s[i]) < ord(t[j]):
        #         i += 1
        #         ans += 1
        #     elif ord(s[i]) > ord(t[j]):
        #         j += 1
        #     else:
        #         i += 1
        #         j += 1
        # return ans + lenS - i
        
        #### Hash Map ####
        # def frequencyMap(s):
        #     freq = {}
        #     for c in s:
        #         if c in freq:
        #             freq[c] += 1
        #         if c not in freq:
        #             freq[c] = 1
        #     return freq
        # ans = 0
        # sMap, tMap = frequencyMap(s), frequencyMap(t)
        # for key in sMap:
        #     if key in tMap:
        #         if sMap[key] > tMap[key]:
        #             ans += sMap[key] - tMap[key]
        #     else:
        #         ans += sMap[key]
        # return ans
        
        #### Counter ####
        S = collections.Counter(s)
        T = collections.Counter(t)
        return sum((S - T).values())