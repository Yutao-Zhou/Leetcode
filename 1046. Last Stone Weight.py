class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ##### really doing it #######
        # while 1:
        #     if len(stones) <= 1:
        #         return stones[0]
        #     stones.sort(reverse = True)
        #     i = 1
        #     while 1:
        #         if i >= len(stones):
        #             break
        #         stones [i - 1] = stones[i - 1] - stones[i]
        #         stones.pop(i)
        #         i += 1
        #         break
        
        ##### another way of doing it #####
        i = 0
        while 1:
            if len(stones) <= 1:
                return stones[0]
            stones.sort(reverse = True)
            stones[1] = stones[0] - stones[1]
            stones.pop(0)