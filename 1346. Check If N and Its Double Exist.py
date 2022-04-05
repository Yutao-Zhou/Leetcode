class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #### check all ####
        # for i in range(len(arr)):
        #     for j in range(i + 1, len(arr)):
        #         if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
        #             return True
        # return False
        
        #### check in there ####
        while arr:
            i = arr.pop()
            if i / 2 in arr or i * 2 in arr:
                return True
        return False