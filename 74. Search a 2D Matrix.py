class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #### cheating ####
        # numbers = []
        # for row in matrix:
        #     numbers += row
        # return target in set(numbers)
        
        #### two binary search ####
        i, j = 0, len(matrix) - 1
        while j - i > 1:
            mid = (i + j) // 2
            if target == matrix[mid][0] or target == matrix[i][0] or target == matrix[j][0]:
                return True
            if target > matrix[mid][0]:
                i = mid
            elif target < matrix[mid][0]:
                j = mid
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[i][l] or target == matrix[i][r] or target == matrix[i][mid]:
                return True
            if target > matrix[i][mid]:
                l = mid + 1
            elif target < matrix[i][mid]:
                r = mid - 1
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[j][l] or target == matrix[j][r] or target == matrix[j][mid]:
                return True
            if target > matrix[j][mid]:
                l = mid + 1
            elif target < matrix[j][mid]:
                r = mid - 1
        return False