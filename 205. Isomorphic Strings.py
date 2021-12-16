class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #### dic two pass ####
        # cacheCheck = {}
        # cacheCheckSecond = {}
        # for i in range(len(s)):
        #     if s[i] in cacheCheck:
        #         if t[i] != cacheCheck[s[i]]:
        #             return False
        #     if s[i] not in cacheCheck:
        #         cacheCheck[s[i]] = t[i]
        # for i in range(len(t)):
        #     if t[i] in cacheCheckSecond:
        #         if s[i] != cacheCheckSecond[t[i]]:
        #             print("here")
        #             return False
        #     if t[i] not in cacheCheckSecond:
        #         cacheCheckSecond[t[i]] = s[i]
        # return True
        
        #### one pass ####
        if len(s) != len(t): return False
        mapped_dict = dict()
        for i, c in enumerate(s):
            if c in mapped_dict:
                if mapped_dict[c] != t[i]:
                    return False
            else:
                if t[i] in list(mapped_dict.values()):
                    return False
                mapped_dict[c] = t[i]
        return True              