class Solution:
    def tribonacci(self, n: int) -> int:
        #### recursive ####
        # def recursive(n):
        #     if n == 0:
        #         return 0
        #     if n == 1 or n == 2:
        #         return 1
        #     else:
        #         return recursive(n - 3) + recursive(n - 2) + recursive(n - 1)
        # return recursive(n)
        
        #### loop without thinking ####
        # if n == 0:
        #     return 0
        # ans = [0, 1, 1]
        # while n >= len(ans):
        #     ans.append(ans[-1] + ans[-2] + ans[-3])
        # return ans[-1]
        
        #### loop with less memory ####
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # ans = (0, 1, 1)
        # n -= 2
        # while n:
        #     ans = (ans[-2], ans[-1], ans[-1] + ans[-2] + ans[-3])
        #     n -= 1
        # return ans[-1]
        
        #### recursive with memorization ####
        cache = {}
        def recursive(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in cache:
                pass
            else:
                cache[n] = recursive(n - 3) + recursive(n - 2) + recursive(n - 1)
            return cache[n]
        return recursive(n)