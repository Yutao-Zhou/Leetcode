class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #### Two Pointer ####
        i, j = 0, 0
        while i < len(arr) and arr[i] < x:
            i += 1
            j += 1
        while j - i <= k:
            if i == -1:
                j += 1
            elif j == len(arr):
                i -= 1
            elif abs(arr[i] - x) <= abs(arr[j] - x):
                i -= 1
            else:
                j += 1
        return arr[i + 1 : j]