class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        #### Frequency table ####
        ans, freqTable = [0, 0], {}
        for c in nums:
            if c in freqTable:
                freqTable[c] += 1
            if c not in freqTable:
                freqTable[c] = 1
        for n in freqTable.values():
            ans[0] += n // 2
            ans[1] += n % 2
        return ans