class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            c = nums2.index(i)
            for j in range(c,len(nums2),1):
                if nums2[j] > i:
                    ans.append(nums2[j])
                    break
                if j == len(nums2) - 1:
                    ans.append(-1)
        return ans