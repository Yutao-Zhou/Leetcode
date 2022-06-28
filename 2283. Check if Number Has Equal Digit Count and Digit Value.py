class Solution:
    def digitCount(self, num: str) -> bool:
        #### Hash table ####
        freqDic = {}
        for n in num:
            n = int(n)
            if n in freqDic:
                freqDic[n] += 1
            if n not in freqDic:
                freqDic[n] = 1
        for idn, n in enumerate(num):
            n = int(n)
            if idn not in freqDic:
                if n != 0:
                    return False
            elif freqDic[idn] != n:
                return False
        return True