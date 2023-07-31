class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        seen = set()
        out_neighbor = {}
        in_neighbor = {}
        queue = deque()
        queue.append(0)
        for i in connections:
            if i[0] in out_neighbor:
                out_neighbor[i[0]].append(i[1])
            if i[0] not in out_neighbor:
                out_neighbor[i[0]] = [i[1]]
            if i[1] in in_neighbor:
                in_neighbor[i[1]].append(i[0])
            if i[1] not in in_neighbor:
                in_neighbor[i[1]] = [i[0]]
        while queue:
            current = queue.popleft()
            if current in out_neighbor:
                for neighbor in out_neighbor[current]:
                    if neighbor not in seen:
                        queue.append(neighbor)
                        ans += 1
            if current in in_neighbor:
                for neighbor in in_neighbor[current]:
                    if neighbor not in seen:
                        queue.append(neighbor)
            seen.add(current)
        return ans