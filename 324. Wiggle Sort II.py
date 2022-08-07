class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #### Sort and merge ####
        s = sorted(nums)
        lower = s[:(len(s) + 1) // 2][::-1]
        upper = s[(len(s) + 1) // 2:][::-1]
        i, j, k = 0, 0, 0
        while k < len(nums):
            if k % 2 == 0:
                nums[k] = lower[i]
                i += 1
                k += 1
            else:
                nums[k] = upper[j]
                j += 1
                k += 1