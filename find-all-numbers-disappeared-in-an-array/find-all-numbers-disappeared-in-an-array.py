class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums = set(nums)
        ck = set(range(1,l + 1))
        return ck.difference(nums)