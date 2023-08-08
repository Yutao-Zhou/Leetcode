class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #### BFS find disconnected ####
        # if len(connections) < n - 1:
        #     return -1
        # m = {}
        # for c in connections:
        #     if c[0] in m:
        #         m[c[0]].append(c[1])
        #     if c[1] in m:
        #         m[c[1]].append(c[0])
        #     if c[0] not in m:
        #         m[c[0]] = [c[1]]
        #     if c[1] not in m:
        #         m[c[1]] = [c[0]]
        # seen = set()
        # cluster = 0
        # for i in range(n):
        #     if i not in seen:
        #         cluster += 1
        #         que = deque([i])
        #         while que:
        #             current = que.popleft()
        #             if current not in seen:
        #                 seen.add(current)
        #                 if current in m:
        #                     for connect in m[current]:
        #                         que.append(connect)
        # return cluster - 1
        
        #### BFS calcualte group and number of connection ####
        num_group = 0
        num_edge = 0
        graph = {}
        start = [False] * n
        for edge in connections:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]
            num_edge += 1
        for i in range(n):
            if start[i] == False:
                stack = [i]
                while stack:
                    current = stack.pop()
                    if start[current] == False:
                        if current in graph:
                            stack.extend(graph[current])
                        start[current] = True
                num_group += 1
        if num_edge < n - 1:
            return -1
        else:
            return num_group - 1