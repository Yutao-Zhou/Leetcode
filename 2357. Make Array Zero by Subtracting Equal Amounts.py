class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        #### Count unique number ####
        # seen = set()
        # for n in nums:
        #     if n != 0:
        #         seen.add(n)
        # return len(seen)

        #### Heap ####
        import heapq
        ans = 0
        heapq.heapify(nums)
        while nums:
            last = heapq.heappop(nums)
            while nums and nums[0] == last:
                heapq.heappop(nums)
            if last != 0:
                ans += 1
        return ans