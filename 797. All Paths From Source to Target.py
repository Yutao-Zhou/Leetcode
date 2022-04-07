class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #### BFS ####
        # target = len(graph) - 1
        # que = deque()
        # que.append((0, [0]))
        # ans = []
        # while que:
        #     cur = que.popleft()
        #     if cur[0] == target:
        #             ans.append(cur[1])
        #     for i in graph[cur[0]]:
        #         que.append((i,cur[1] + [i]))
        # return ans
        
        #### DFS ####
        target = len(graph) - 1
        stack = [(0, [0])]
        ans = []
        while stack:
            cur = stack.pop()
            if cur[0] == target:
                    ans.append(cur[1])
            for i in graph[cur[0]]:
                stack.append((i,cur[1] + [i]))
        return ans