class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        #### DFS ####
        ans = 0
        stack = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    stack.append((i, j))
                    ans += 1
                    while stack:
                        node = stack.pop()
                        if 0 <= node[0] < len(board) and 0 <= node[1] < len(board[0]):
                            if board[node[0]][node[1]] == "X":
                                board[node[0]][node[1]] = "."
                                stack.append((node[0] - 1, node[1]))
                                stack.append((node[0], node[1] + 1))
                                stack.append((node[0] + 1, node[1]))
                                stack.append((node[0], node[1] - 1))
        return ans