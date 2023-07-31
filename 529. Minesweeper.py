class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        #### BFS ####
        seen = set()
        m = len(board)
        n = len(board[0])
        ans = board
        queue = deque()
        queue.append((click[0], click[1]))
        dxdy = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        if board[click[0]][click[1]] == "M":
            ans[click[0]][click[1]] = "X"
            return ans
        while queue:
            current = queue.popleft()
            y, x = current[0], current[1]
            if current not in seen:
                digit = 0
                tmp = []
                for neighbor in dxdy:
                    if 0 <= y + neighbor[0] < m and 0 <= x + neighbor[1] < n:
                        if board[y + neighbor[0]][x + neighbor[1]] == "M":
                            digit += 1
                        tmp.append((y + neighbor[0], x + neighbor[1]))
                if digit == 0:
                    queue.extend(tmp)
                    ans[y][x] = "B"
                else:
                    ans[y][x] = str(digit)
                seen.add(current)
        return ans