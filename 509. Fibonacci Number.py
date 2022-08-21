class Solution:
    def fib(self, n: int) -> int:
        ##### raw solve ####
        # cach1 = 0
        # cach2 = 1
        # ans = 0
        # i = 2
        # if n < 2:
        #     return n
        # else:
        #     while i <= n:
        #         ans = cach1 + cach2
        #         cach1 = cach2
        #         cach2 = ans
        #         i += 1
        # return ans
    
        #### math ####
        # Phi = (1 + 5 ** 0.5) / 2
        # phi = (1 - 5 ** 0.5) / 2
        # return int((Phi ** n - phi ** n) / 5 ** 0.5)
    
        #### recursive ####
        # def recursive(n):
        #     if n == 0:
        #         return 0
        #     if n == 1:
        #         return 1
        #     else:
        #         return recursive(n - 1) + recursive(n - 2)
        # return recursive(n)
        
        #### recursive with memorization ####
        cache = {}
        def recursive(n):
            if n < 2:
                return n
            if n in cache:
                pass
            else:
                cache[n] = recursive(n - 1) + recursive(n - 2)
            return cache[n]
        return recursive(n)