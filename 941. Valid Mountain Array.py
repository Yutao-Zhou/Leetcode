class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ###### find peak and judge #####
        # max = 0
        # maxIndex = 0
        # for i in range(len(arr)):
        #     if arr[i] > max:
        #         max = arr[i]
        #         maxIndex = i
        # if maxIndex == 0 or maxIndex == len(arr) - 1:
        #     return False
        # for i in range(1,maxIndex + 1):
        #     if arr[i] <= arr[i - 1]:
        #         return False
        # for i in range(maxIndex + 1,len(arr)):
        #     if arr[i] >= arr[i - 1]:
        #         return False
        # return True
        
        ###### smart find peak ####
        peak = arr.index(max(arr))
        if peak == 0 or peak == len(arr) - 1:
            return False
        uphill = arr[:peak + 1]
        downhill = arr[peak:]
        if sorted(list(set(uphill))) != uphill:
            return False
        if sorted(downhill,reverse = True) != downhill or sorted(list(set(downhill))) != sorted(downhill):
            return False
        else:
            return True