class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #### Backtrack ####
        # def climb(start, c):
        #     if start == len(cost):
        #         nonlocal ans
        #         ans = min(ans, c)
        #         return
            
        #     climb(start + 1, c + cost[start])
        #     if start + 2 <= len(cost):
        #         climb(start + 2, c + cost[start])
        
        # ans = sum(cost)
        # climb(0, 0)
        # climb(1, 0)
        # return ans

        #### DP top down ####
        # def climb(start):
        #     if start <= 1:
        #         return 0
            
        #     if memo[start] != 0:
        #         return memo[start]

        #     result_one = cost[start - 1] + climb(start - 1)
        #     result_two = cost[start - 2] + climb(start - 2)
        #     memo[start] = min(result_one, result_two)
        #     return memo[start]
        
        # memo = [0] * (len(cost) + 1)
        # return climb(len(cost))

        #### DP Bottom Up ####
        # memo = [sum(cost) + 1] * (len(cost) + 2)
        # memo[0], memo[1] = 0, 0
        # for i in range(len(cost)):
        #     memo[i + 1] = min(memo[i + 1], memo[i] + cost[i])
        #     memo[i + 2] = min(memo[i + 2], memo[i] + cost[i])
        # return memo[-2]

        #### DP Bottom Up constant space####
        last_one, last_two = 0, 0
        for i in range(2, len(cost) + 1):
            current = min(last_one + cost[i - 1], last_two + cost[i - 2])
            last_two = last_one
            last_one = current
        return current