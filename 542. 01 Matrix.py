class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #### Brute Force BFS ####
        # def BFS(mat, ans, start):
        #     visited = set()
        #     que = deque()
        #     que.append((start[0], start[1], 0))
        #     while que:
        #         node = que.popleft()
        #         if node not in visited:
        #             i = node[0]
        #             j = node[1]
        #             d = node[2]
        #             visited.add(node)
        #             if 0 <= i < len(mat[0]) and 0 <= j < len(mat):
        #                 if mat[i][j] == 0:
        #                     ans[start[0]][start[1]] = d
        #                     return ans
        #                 elif mat[i][j] == 1:
        #                     que.append((i, j - 1, d + 1))
        #                     que.append((i + 1, j, d + 1))
        #                     que.append((i, j + 1, d + 1))
        #                     que.append((i - 1, j, d + 1))
        # ans = mat
        # for x in range(len(mat)):
        #     for y in range(len(mat[0])):
        #         if mat[x][y] != 0:
        #             BFS(mat, ans, (x, y))
        # return ans
        
        #### BFS From 0 ####
        # queue, ans, visited = deque(), [[0] * len(mat[0]) for i in range(len(mat))], set()
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j] == 0:
        #             queue.append((i, j, 0))
        # while queue:
        #     node = queue.popleft()
        #     if (node[0], node[1]) not in visited:
        #         visited.add((node[0], node[1]))
        #         if mat[node[0]][node[1]] == 1:
        #             ans[node[0]][node[1]] = node[2]
        #         if 0 <= node[0] - 1:
        #             queue.append((node[0] - 1, node[1], node[2] + 1))
        #         if 0 <= node[1] - 1:
        #             queue.append((node[0], node[1] - 1, node[2] + 1))
        #         if node[0] + 1 < len(mat):
        #             queue.append((node[0] + 1, node[1], node[2] + 1))
        #         if node[1] + 1 < len(mat[0]):
        #             queue.append((node[0], node[1] + 1, node[2] + 1))
        # return ans
        
        #### DP ####
        m, n = len(mat), len(mat[0])
        ans = [[float('inf')] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if 0 <= i - 1:
                        ans[i][j] = ans[i - 1][j] + 1
                    if 0 <= j - 1:
                        ans[i][j] = min(ans[i][j], ans[i][j - 1] + 1)
                else:
                    ans[i][j] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] == 1:
                    if i + 1 < m:
                        ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1)
                    if j + 1 < n:
                        ans[i][j] = min(ans[i][j], ans[i][j + 1] + 1)
                else:
                    ans[i][j] = 0
        return ans