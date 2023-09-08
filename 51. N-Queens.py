class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(board, row, column):
            for i in range(row):
                for j in range(n):
                    if (row - i == abs(column - j) or i == row or j == column) and board[i][j] == 'Q':
                        return False
            return True

        def queen(board, row):
            if row == n:
                ans.append(board.copy())
                return
            for c in range(n):
                if is_valid(board, row, c):
                    board.append('.' * c + 'Q' + '.' * (n - c - 1))
                    queen(board, row + 1)
                    board.pop()
            
        ans = []
        queen([], 0)
        return ans