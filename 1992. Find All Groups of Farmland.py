class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        #### BFS ####
        join = []
        cache = []
        ans = []
        for i in range(len(land)):
            for j in range(len(land[i])):
                if land[i][j] == 1:
                    que = deque()
                    que.append((i,j))
                    join.append(i)
                    join.append(j)
                    while que:
                        node = que.popleft()
                        if 0 <= node[0] < len(land) and 0 <= node[1] < len(land[i]) and land[node[0]][node[1]] == 1:
                            land[node[0]][node[1]] = -1
                            que.append((node[0] - 1,node[1]))
                            que.append((node[0],node[1] + 1))
                            que.append((node[0] + 1,node[1]))
                            que.append((node[0],node[1] - 1))
                            cache.append(node[0])
                            cache.append(node[1])
                    join.append(cache[-2])
                    join.append(cache[-1])
                    cache = []
                    ans.append(join)
                    join = []
        return ans