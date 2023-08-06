class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        #### DFS ####
        ans = 0
        seen = [0] * n
        graph = {}
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]
        for i in range(n):
            if seen[i] == 0:
                num_node = 0
                num_edge = 0
                queue = [i]
                while queue:
                    current = queue.pop()
                    if seen[current] == 0:
                        num_node += 1
                        seen[current] = 1
                        if current in graph:
                            queue.extend(graph[current])
                            num_edge += len(graph[current])
                if num_edge == num_node * (num_node - 1):
                    ans += 1
        return ans