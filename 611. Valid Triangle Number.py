class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #### linear search ####
        # ans = 0
        # len_nums = len(nums)
        # nums.sort()
        # for i in range(len_nums):
        #     for j in range(i + 2, len_nums):
        #         l, r = i + 1, j - 1
        #         while l < len_nums and not nums[j] - nums[i] < nums[l]:
        #             l += 1
        #         while r > -1 and not nums[r] < nums[j] + nums[i]:
        #             r -= 1
        #         if l <= r:
        #             ans += r - l + 1
        # return ans

        #### Brute Force ####
        # ans = 0
        # nums.sort()
        # len_nums = len(nums)
        # for i in range(len_nums - 2):
        #     for j in range(i + 1, len_nums -1):
        #         for k in range(j + 1, len_nums):
        #             if nums[i] + nums[j] > nums[k] and nums[j] + nums[k] > nums[i] and nums[i] + nums[k] > nums[j]:
        #                 ans += 1
        # return ans

        #### linear search ####
        ans = 0
        len_nums = len(nums)
        nums.sort()
        for i in range(len_nums - 2):
            if nums[i] != 0:
                k = i + 2
                for j in range(i + 1, len_nums - 1):
                    while k < len_nums and nums[i] + nums[j] > nums[k]:
                        k += 1
                    ans += k - j - 1
        return ans