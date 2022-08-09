class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #### Map to Dictionary ####
        # row, column, square = {}, {}, {}
        # for i in range(9):
        #     row[i] = set()
        #     column[i] = set()
        # for i in range(3):
        #     for j in range(3):
        #         square[(i,j)] = set()
        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] != ".":
        #             if board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in square[r // 3, c // 3]:
        #                 return False
        #             row[r].add(board[r][c])
        #             column[c].add(board[r][c])
        #             square[(r // 3, c // 3)].add(board[r][c])
        # return True
        
        #### Map with list ####
        row, column, square = [], [], []
        for _ in range(9):
            row.append(set())
            column.append(set())
        for _ in range(3):
            cache = []
            for _ in range(3):
                cache.append(set())
            square.append(cache)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in square[r // 3][c // 3]:
                        return False
                    row[r].add(board[r][c])
                    column[c].add(board[r][c])
                    square[r // 3][c // 3].add(board[r][c])
        return True