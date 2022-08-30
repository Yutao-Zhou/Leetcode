class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #### Brute Force Sort and Two Pointers Compare ####
        # i, j, ans = 0, 0, [[], []]
        # nums1 = sorted(list(set(nums1)))
        # nums2 = sorted(list(set(nums2)))
        # il, jl = len(nums1), len(nums2)
        # while i < il and j < jl:
        #     if nums1[i] == nums2[j]:
        #         i += 1
        #         j += 1
        #     elif nums1[i] < nums2[j]:
        #         ans[0].append(nums1[i])
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         ans[1].append(nums2[j])
        #         j += 1
        # if i < il:
        #     ans[0].extend(nums1[i:])
        # if j < jl:
        #     ans[1].extend(nums2[j:])
        # return ans
        
        #### Set ####
        return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]