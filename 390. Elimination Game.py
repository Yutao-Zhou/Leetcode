class Solution:
    def lastRemaining(self, n: int) -> int:
        #### Brute Force Simulation ####
        # counter, cache1, cache2 = 0, deque([*range(1, n + 1)]), deque()
        # while len(cache1) != 1 and len(cache2) != 1:
        #     if counter % 2:
        #         for i in range(len(cache1)):
        #             if i % 2:
        #                 cache2.append(cache1[i])
        #         cache1 = deque()
        #     elif not counter % 2:
        #         for i in range(len(cache2) - 1, -1, -1):
        #             if not i % 2:
        #                 cache1.appendleft(cache2[i])
        #         cache2 = deque()
        #     counter += 1
        # if cache1:
        #     return cache1[0]
        # return cache2[0]
        
        #### Recursion ####
        def helper(n, isLeft):
            if n == 1:
                return 1
            if isLeft:
                return 2 * helper(n // 2, 0)
            elif n % 2 == 1:
                return 2 * helper(n // 2, 1)
            return 2 * helper(n // 2, 1) - 1
        return helper(n, 1)