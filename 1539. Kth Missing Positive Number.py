class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ##### not solving the problem by set #####
        # check = set(list(range(2001)))
        # arr = set(arr)
        # difference = check.difference(arr)
        # return list(difference)[k]
        
        ##### real solution #####
        i = 1
        counter = 0
        if arr[0] != 1:
                arr.insert(0,1)
                counter += 1
        while 1:
            if counter == k:
                return arr[i - 1]
            if i >= len(arr):
                arr.append(arr[i - 1] + 1)
                counter += 1
            elif arr[i] != arr[i - 1] + 1 and i < len(arr):
                arr.insert(i,arr[i - 1] + 1)
                counter += 1
            i += 1            