class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        #### BFS store path and check ####
        # ans = 0
        # cache = []
        # for i in range(len(grid2)):
        #     for j in range(len(grid2[i])):
        #         if grid2[i][j] == 1:
        #             que = deque()
        #             que.append((i,j))
        #             while que:
        #                 node = que.popleft()
        #                 if 0 <= node[0] < len(grid2) and 0 <= node[1] < len(grid2[i]) and grid2[node[0]][node[1]] == 1:
        #                     grid2[node[0]][node[1]] = -1
        #                     que.append((node[0] - 1, node[1]))
        #                     que.append((node[0], node[1] + 1))
        #                     que.append((node[0] + 1, node[1]))
        #                     que.append((node[0], node[1] - 1))
        #                     cache.append(node)
        #             if cache:
        #                 for pair in cache:
        #                     if grid1[pair[0]][pair[1]] != 1:
        #                         ans -= 1
        #                         break
        #                 ans += 1
        #                 cache = []
        # return ans
        
        #### BFS check while iterating ####
        from collections import deque
        ans = 0
        disgard = False
        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                if grid2[i][j] == 1 and grid1[i][j] == 1:
                    que = deque()
                    que.append((i,j))
                    abandon = False
                    while que:
                        node = que.popleft()
                        if 0 <= node[0] < len(grid2) and 0 <= node[1] < len(grid2[i]) and grid2[node[0]][node[1]] == 1:
                            if grid1[node[0]][node[1]] != 1:
                                abandon = True
                            grid2[node[0]][node[1]] = -1
                            que.append((node[0] - 1, node[1]))
                            que.append((node[0], node[1] + 1))
                            que.append((node[0] + 1, node[1]))
                            que.append((node[0], node[1] - 1))
                    if abandon == False:
                        ans += 1
        return ans