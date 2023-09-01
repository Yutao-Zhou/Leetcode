class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        #### Heap ####
        import heapq
        ans = 0
        heap = []
        heapq.heappush(heap, -a)
        heapq.heappush(heap, -b)
        heapq.heappush(heap, -c)
        while len(heap) > 1:
            pile1 = heapq.heappop(heap) + 1
            pile2 = heapq.heappop(heap) + 1
            if pile1 != 0:
                heapq.heappush(heap, pile1)
            if pile2 != 0:
                heapq.heappush(heap, pile2)
            ans += 1
        return ans