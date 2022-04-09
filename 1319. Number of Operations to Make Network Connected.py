class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #### BFS find disconnected ####
        if len(connections) < n - 1:
            return -1
        m = {}
        for c in connections:
            if c[0] in m:
                m[c[0]].append(c[1])
            if c[1] in m:
                m[c[1]].append(c[0])
            if c[0] not in m:
                m[c[0]] = [c[1]]
            if c[1] not in m:
                m[c[1]] = [c[0]]
        seen = set()
        cluster = 0
        for i in range(n):
            if i not in seen:
                cluster += 1
                que = deque([i])
                while que:
                    current = que.popleft()
                    if current not in seen:
                        seen.add(current)
                        if current in m:
                            for connect in m[current]:
                                que.append(connect)
        return cluster - 1