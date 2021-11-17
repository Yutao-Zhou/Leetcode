class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # i = 0
        # while 1:
        #     if i == len(arr) or i == len(arr) + 1:
        #         break
        #     if arr[i] == 0:
        #         arr.insert(i,0)
        #         arr.pop()
        #         i += 2
        #     else:
        #         i += 1
        z = arr.count(0)
        for i in range(-1,-len(arr),-1):
            if i + z < len(arr):
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0