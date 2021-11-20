class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ########set#########
        # nums1 = set(nums1)
        # nums2 = set(nums2)
        # return nums1.intersection(nums2)
        
        #####sort check#####
        # i = 0
        # j = 0
        # ans = []
        # nums1.sort()
        # nums2.sort()
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         if nums1[i] not in ans:
        #             ans.append(nums1[i])
        #         i += 1
        #         j += 1
        # return ans
        
        ######check no dic ########
        ans = []
        if len(nums1) >= len(nums2):
            for i in nums2:
                if i in nums1 and i not in ans:
                    ans.append(i)
        else:
            for i in nums1:
                if i in nums2 and i not in ans:
                    ans.append(i)
        return ans