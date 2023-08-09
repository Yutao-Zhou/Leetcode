class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        #### Brute Force ####
        # ans = 0
        # i_length = len(nums1)
        # j_length = len(nums2)
        # for i in range(len(nums1)):
        #     for j in range(i, len(nums2)):
        #         if nums1[i] <= nums2[j]:
        #             ans = max(ans, j - i)
        #         else:
        #             break
        # return ans

        #### two pointer ####
        ans = 0
        i, j = 0, 0
        i_length = len(nums1)
        j_length = len(nums2)
        while i < i_length and j < j_length:
            while j < j_length and nums1[i] <= nums2[j]:
                j += 1
            ans = max(ans, j - i - 1)
            i += 1
        return ans