class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        #### No thinking simulation ####
        while original in nums:
            original *= 2
        return original