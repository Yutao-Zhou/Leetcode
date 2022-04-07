class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        #### map two pass ####
        row = []
        column = []
        for r in matrix:
            row.append(min(r))
        for i in range(len(matrix[0])):
            maximum = 1
            for r in matrix:
                if r[i] > maximum:
                    maximum = r[i]
            column.append(maximum)
        return set(row) & set(column)