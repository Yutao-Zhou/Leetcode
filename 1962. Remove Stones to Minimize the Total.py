class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        #### Greedy Heap ####
        import heapq
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for i in range(k):
            current = heapq.heappop(piles)
            current -= int(current / 2)
            heapq.heappush(piles, current)
        return -sum(piles)