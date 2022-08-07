class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #### Binary search ####
        def countSmallerOrEqual(mid):
            smallerOrEqual = 0
            row, right = 0, len(matrix) - 1
            while row < len(matrix):
                while matrix[row][right] > mid and right > -1:
                    right -= 1
                if right == -1:
                    break
                else:
                    smallerOrEqual += right + 1
                    row += 1
            return smallerOrEqual
        low, high = matrix[0][0], matrix[-1][-1]
        while low <= high:
            mid = (high + low) // 2
            hit = countSmallerOrEqual(mid)
            if hit < k:
                low = mid + 1
            if hit >= k:
                high = mid - 1
        return low