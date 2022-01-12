class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #### replace again and again ####
        # for i in range(len(arr)):
        #     arr[i] = -1
        #     for j in range(i + 1, len(arr)):
        #         if arr[j] > arr[i]:
        #             arr[i] = arr[j]
        # return arr
        
        #### faster way ####
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr