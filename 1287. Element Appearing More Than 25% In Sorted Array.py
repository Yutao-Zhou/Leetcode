class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # return max(arr,key = arr.count)
        
        # counter = {}
        # for i in arr:
        #     if i in counter:
        #         counter[i] += 1
        #     if i not in counter:
        #         counter[i] = 1
        #     if max(counter.values()) > len(arr)/4:
        #         return i
        
        
        # counter = 1
        # for i in range(len(arr)):
        #     if arr[i] == arr[i-1]:
        #         counter += 1
        #         if counter > len(arr)/4:
        #             return arr[i]
        #     else: 
                    # counter = 1
        
        
        # r = arr.copy()
        # r.reverse()
        # if len(arr) <= 3:
        #     return arr[0]
        # else:
        #     a = arr[int(len(arr)/4)]
        #     b = arr[int(len(arr)/2)]
        #     c = arr[int(len(arr)*3/4)]
        #     if abs(len(arr)-r.index(a) - arr.index(a)) > len(arr)/4:
        #         return a
        #     if abs(len(arr)-r.index(b) - arr.index(b)) > len(arr)/4:
        #         return b
        #     if abs(len(arr)-r.index(c) - arr.index(c)) > len(arr)/4:
        #         return c