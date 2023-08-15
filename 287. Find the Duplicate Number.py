class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #### Binary Search ####
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            target = (l + r) // 2
            counter = 0
            for n in nums:
                if n <= target:
                    counter += 1
            if counter > target:
                ans = target
                r = target
            else:
                l = target + 1
        return r