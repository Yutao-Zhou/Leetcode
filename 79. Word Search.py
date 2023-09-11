class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #### Backtrack ####
        def findWord(pointer, x, y):
            if pointer == len(word):
                nonlocal ans
                ans = True
                return True

            if x - 1 >= 0 and board[y][x - 1] == word[pointer]:
                board[y][x - 1] = ""
                if findWord(pointer + 1, x - 1, y):
                    return True
                board[y][x - 1] = word[pointer]
            if x + 1 < len(board[0]) and board[y][x + 1] == word[pointer]:
                board[y][x + 1] = ""
                if findWord(pointer + 1, x + 1, y):
                    return True
                board[y][x + 1] = word[pointer]
            if y - 1 >= 0 and board[y - 1][x] == word[pointer]:
                board[y - 1][x] = ""
                if findWord(pointer + 1, x, y - 1):
                    return True
                board[y - 1][x] = word[pointer]
            if y + 1 < len(board) and board[y + 1][x] == word[pointer]:
                board[y + 1][x] = ""
                if findWord(pointer + 1, x, y + 1):
                    return True
                board[y + 1][x] = word[pointer]
        
        ans = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = ""
                    findWord(1, j, i)
                    board[i][j] = word[0]
        return ans