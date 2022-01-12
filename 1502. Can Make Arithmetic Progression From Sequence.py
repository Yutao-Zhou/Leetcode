class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        #### sort and check ####
        # arr.sort()
        # difference = arr[1] - arr[0]
        # for i in range(1,len(arr)):
        #     if arr[i] - arr[i - 1] != difference:
        #         return False
        # return True
        
        #### find average distance ####
        difference = (max(arr) - min(arr)) // (len(arr) - 1)
        if (max(arr) - min(arr)) % (len(arr) - 1) != 0:
            return False
        elif difference == 0:
            return True
        elif len(set(arr)) != len(arr):
            return False
        for i in range(1,len(arr)):
            if (arr[i] - min(arr)) % difference != 0:
                return False
        return True