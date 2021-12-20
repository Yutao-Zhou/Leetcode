class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDifference = 10 ** 7
        ans = []
        for i in range(1,len(arr)):
            if arr[i] - arr[i - 1] < minDifference:
                minDifference = arr[i] - arr[i - 1]
                ans = []
            if arr[i] - arr[i - 1] == minDifference:
                ans.append([arr[i - 1],arr[i]])
        return ans