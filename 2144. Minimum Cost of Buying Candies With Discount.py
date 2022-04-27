class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        #### sort itertive greedy ####
        # cost = sorted(cost)
        # ans = 0
        # for i in range(-1, -(len(cost)) - 1, -1):
        #     if i % 3 != 0:
        #         ans += cost[i]
        # return ans
        
        #### sort recursive ####
        cost = sorted(cost)
        def recursion(i, ans):
            if i == -len(cost) - 1:
                return ans
            if i % 3 != 0:
                return recursion(i - 1, ans + cost[i])
            if i % 3 == 0:
                return recursion(i - 1, ans)
        return recursion(-1, 0)