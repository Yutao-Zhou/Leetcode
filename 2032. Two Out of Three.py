class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ck = {}
        ans = []
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        for i in nums1:
            ck[i] = 1
        for i in nums2:
            if i in ck:
                ck[i] += 1
            if i not in ck:
                ck[i] = 1
        for i in nums3:
            if i in ck:
                ck[i] += 1
            if i not in ck:
                ck[i] = 1
        for i,k in ck.items():
            if k >= 2:
                ans.append(i)
        return ans