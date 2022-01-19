class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        #### set ####
        vertical = []
        for i in range(len(matrix)):
            if len(set(matrix[i])) != len(matrix):
                return False
            for j in matrix:
                vertical.append(j[i])
            if len(set(vertical)) != len(matrix):
                return False
            vertical = []
        return True