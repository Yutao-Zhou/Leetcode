class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #### Min heap ####
        import heapq
        flight_map = {}
        for s, d, w in flights:
            if s in flight_map:
                flight_map[s].append((d, w))
            else:
                flight_map[s] = [(d, w)]

        queue = []
        min_step = [float(inf)] * n
        if src in flight_map:
            for d, w in flight_map[src]:
                queue.append((w, d, 0))
        heapq.heapify(queue)
        while queue:
            weight, city, transit = heapq.heappop(queue)
            if transit <= k:
                if city == dst:
                    return weight
                elif min_step[city] > transit and city in flight_map:
                    for d, w in flight_map[city]:
                        heapq.heappush(queue, (weight + w, d, transit + 1))
                    min_step[city] = transit
        return -1