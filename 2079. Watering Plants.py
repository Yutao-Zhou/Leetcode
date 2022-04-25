class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        #### simulation ####
        # i = 0
        # bucket = capacity
        # ans = 0
        # while i < len(plants):
        #     if bucket >= plants[i]:
        #         bucket -= plants[i]
        #         ans += 1
        #         i += 1
        #     else:
        #         bucket = capacity
        #         ans += 2 * i
        # return ans
        
        #### recursive ####
        def recursion(i, bucket, ans):
            if i >= len(plants):
                return ans
            elif plants[i] <= bucket:
                return recursion(i + 1, bucket - plants[i], ans + 1)
            else:
                return recursion(i, capacity, ans + (2 * i))
        return recursion(0, capacity, 0)