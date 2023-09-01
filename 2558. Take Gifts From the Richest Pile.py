class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        #### Heap Simulation ####
        import heapq
        gifts = [-x for x in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            gift = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(gift ** 0.5))
        return -sum(gifts)