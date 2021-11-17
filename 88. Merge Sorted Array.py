class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = len(nums2) - 1
        k = len(nums1) - 1
        while 1:
            print(i,j,k)
            print(nums1,nums2)
            if i > -1 and j > -1:
                if nums2[j] >= nums1[i]:
                    nums1[k] = nums2[j]
                    j -= 1
                    k -= 1
                if nums2[j] < nums1[i]:
                    nums1[k] = nums1[i]
                    i -= 1
                    k -= 1
            elif i == -1 and j >-1:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
            else:
                break