class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        #### Brute Force ####
        # for i in range(n, n * 2 + 1):
        #     if not i % n and not i % 2:
        #         return i
        
        #### Even Odd ####
        if n % 2:
            return 2 * n
        return n