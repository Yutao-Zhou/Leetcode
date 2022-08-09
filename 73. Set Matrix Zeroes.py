class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #### Brute Force ####
        # zeros = []
        # for row in range(len(matrix)):
        #     for column in range(len(matrix[row])):
        #         if matrix[row][column] == 0:
        #             zeros.append((row, column))
        # while zeros:
        #     current = zeros.pop()
        #     matrix[current[0]] = [0] * len(matrix[current[0]])
        #     for i in range(len(matrix)):
        #         matrix[i][current[1]] = 0
        
        #### set zero to start O(1) space ####
        nR, nC = len(matrix), len(matrix[0])
        zeroRow = False
        for row in matrix:
            if row[0] == 0:
                zeroRow = True
        zeroColumn = True if 0 in matrix[0] else False
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0
        for i in range(1, nR):
            if matrix[i][0] == 0:
                matrix[i] = [0] * nC
        for i in range(1, nC):
            if matrix[0][i] == 0:
                for j in range(1,nR):
                    matrix[j][i] = 0
        if zeroRow:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        if zeroColumn:
            matrix[0] = [0] * nC