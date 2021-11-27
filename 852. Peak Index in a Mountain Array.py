class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        ##### binary search #####
        # l = 0
        # h = len(arr) - 1
        # while l < h:
        #     m = (l + h) // 2
        #     if arr[m - 1] < arr[m] and arr[m + 1] < arr[m]:
        #         return m
        #     elif arr[m - 1] < arr[m] :
        #         l = m
        #     elif arr[m - 1] > arr[m] :
        #         h = m
        
        ###### one side loop#####
        # for i in range(1,len(arr)):
        #     if arr[i] < arr[i - 1]:
        #         return i - 1
        
        ###### fake solution ######
        return arr.index(max(arr))