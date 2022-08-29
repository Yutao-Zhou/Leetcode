class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #### One by One ####
        # for _ in range(k):
        #     previous = nums[-1] 
        #     for i in range(len(nums)):
        #         temp = nums[i]
        #         nums[i] = previous
        #         previous = temp
        
        #### Reverse ####
        ln = len(nums)
        k %= ln
        for i in range(ln // 2):
            nums[i], nums[ln - i - 1] = nums[ln - i - 1], nums[i]
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
        for i in range(k, (ln + k) // 2):
            nums[i], nums[ln - i + k - 1] = nums[ln - i + k - 1], nums[i]