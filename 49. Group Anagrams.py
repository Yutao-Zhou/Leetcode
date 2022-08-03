class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #### brute force(hashtable) ####
        mapDic = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - 97] += 1
            freq = tuple(freq)
            if freq in mapDic:
                mapDic[freq].append(s)
            if freq not in mapDic:
                mapDic[freq] = [s]
        return mapDic.values()