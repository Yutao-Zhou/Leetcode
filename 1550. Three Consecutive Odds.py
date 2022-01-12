class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        #### check ####
        # if len(arr) < 3:
        #     return False
        # for i in range(2,len(arr)):
        #     if arr[i] % 2 == 1 and arr[i - 1] % 2 == 1 and arr[i - 2] % 2 == 1:
        #         return True
        # return False
        
        #### divide and check####
        for i in range(len(arr)):
            arr[i] = str(arr[i] % 2)
        return "111" in "".join(arr)