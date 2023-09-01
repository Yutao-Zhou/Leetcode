class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        #### Greedy Sort ####
        # ans = 0
        # connection_map = [0] * n
        # for road in roads:
        #     connection_map[road[0]] += 1
        #     connection_map[road[1]] += 1
        # connection_map.sort()
        # for i in range(n):
        #     ans += connection_map[i] * (i + 1)
        # return ans

        #### Greedy Heap ####
        import heapq
        ans = 0
        connection_map = [0] * n
        for road in roads:
            connection_map[road[0]] += 1
            connection_map[road[1]] += 1
        heapq.heapify(connection_map)
        for i in range(n):
            ans += (i + 1) * heapq.heappop(connection_map)
        return ans