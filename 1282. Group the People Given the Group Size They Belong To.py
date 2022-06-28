class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        #### Hash Table ####
        group = {}
        ans = []
        for idn,n in enumerate(groupSizes):
            if n in group:
                group[n].append(idn)
            if n not in group:
                group[n] = [idn]
        for k, v in group.items():
            for i in range(k, len(v) + 1, k):
                ans.append(v[i - k:i])
        return ans