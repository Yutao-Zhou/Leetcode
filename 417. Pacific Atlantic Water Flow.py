class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #### BFS ####
        # def add(node, Ocean):
        #     if 0 <= node[0] < m and 0 <= node[1] < n:
        #         if heights[node[0]][node[1]] >= currAltitde:
        #             queue.append(node)
        #             Ocean[node[0]][node[1]] = True
        # m, n = len(heights), len(heights[0])
        # # Start From Pacific
        # Pacific = [[False] * n for i in range(m)]
        # queue, visit = deque(), set()
        # for i in range(m):
        #     queue.append((i, 0))
        #     Pacific[i][0] = True
        # for j in range(n):
        #     queue.append((0, j))
        #     Pacific[0][j] = True
        # while queue:
        #     node = queue.popleft()
        #     if (node[0], node[1]) not in visit and Pacific[node[0]][node[1]] == True:
        #         visit.add((node[0], node[1]))
        #         currAltitde = heights[node[0]][node[1]]
        #         add((node[0] + 1, node[1]), Pacific)
        #         add((node[0] - 1, node[1]), Pacific)
        #         add((node[0], node[1] + 1), Pacific)
        #         add((node[0], node[1] - 1), Pacific)
        # # Start From Atlantic
        # Atlantic = [[False] * n for i in range(m)]
        # queue, visit = deque(), set()
        # for i in range(m):
        #     queue.append((i, n - 1))
        #     Atlantic[i][n - 1] = True
        # for j in range(n):
        #     queue.append((m - 1, j))
        #     Atlantic[m - 1][j] = True
        # while queue:
        #     node = queue.popleft()
        #     if (node[0], node[1]) not in visit and Atlantic[node[0]][node[1]] == True:
        #         visit.add((node[0], node[1]))
        #         currAltitde = heights[node[0]][node[1]]
        #         add((node[0] + 1, node[1]), Atlantic)
        #         add((node[0] - 1, node[1]), Atlantic)
        #         add((node[0], node[1] + 1), Atlantic)
        #         add((node[0], node[1] - 1), Atlantic)
        # ans = []
        # for i in range(m):
        #     for j in range(n):
        #         if Pacific[i][j] and Atlantic[i][j]:
        #             ans.append((i, j))
        # return ans
        
        #### BFS ####
        def add(node, Ocean):
            if 0 <= node[0] < m and 0 <= node[1] < n:
                if heights[node[0]][node[1]] >= currAltitde:
                    queue.append(node)
                    Ocean[node[0]][node[1]] = True
        m, n = len(heights), len(heights[0])
        # Start From Pacific
        Pacific = [[False] * n for i in range(m)]
        queue, visitP = deque(), set()
        for i in range(m):
            queue.append((i, 0))
            Pacific[i][0] = True
        for j in range(n):
            queue.append((0, j))
            Pacific[0][j] = True
        while queue:
            node = queue.popleft()
            if (node[0], node[1]) not in visitP and Pacific[node[0]][node[1]] == True:
                visitP.add((node[0], node[1]))
                currAltitde = heights[node[0]][node[1]]
                add((node[0] + 1, node[1]), Pacific)
                add((node[0] - 1, node[1]), Pacific)
                add((node[0], node[1] + 1), Pacific)
                add((node[0], node[1] - 1), Pacific)
        # Start From Atlantic
        Atlantic = [[False] * n for i in range(m)]
        queue, visitA = deque(), set()
        for i in range(m):
            queue.append((i, n - 1))
            Atlantic[i][n - 1] = True
        for j in range(n):
            queue.append((m - 1, j))
            Atlantic[m - 1][j] = True
        while queue:
            node = queue.popleft()
            if (node[0], node[1]) not in visitA and Atlantic[node[0]][node[1]] == True:
                visitA.add((node[0], node[1]))
                currAltitde = heights[node[0]][node[1]]
                add((node[0] + 1, node[1]), Atlantic)
                add((node[0] - 1, node[1]), Atlantic)
                add((node[0], node[1] + 1), Atlantic)
                add((node[0], node[1] - 1), Atlantic)
        # Check wither points that can reach one of them can reach both ocean by intersect visited set(only reachble points are visited)
        return visitP.intersection(visitA)