class Solution:
    def climbStairs(self, n: int) -> int:
        #### recursion with memorization ####
        # cache = {}
        # def recursion(remain):
        #     if remain < 3:
        #         return remain
        #     if remain in cache:
        #         pass
        #     else:
        #         cache[remain] = recursion(remain - 1) + recursion(remain - 2)
        #     return cache[remain]
        # return recursion(n)
        
        #### recursion with memorization another way ####
        cache = {1: 1, 2: 2}
        def recursion(remain):
            if remain in cache:
                pass
            else:
                cache[remain] = recursion(remain - 1) + recursion(remain - 2)
            return cache[remain]
        return recursion(n)