class Solution:
    def totalMoney(self, n: int) -> int:
        #### math ####
        # ans = 0
        # if n < 8:
        #     return (1 + n) * n // 2
        # if n >= 8:
        #     ans += n // 7 * 28
        #     ans += ((7 +  (n // 7 - 1) * 7) * (n // 7 - 1)) // 2
        #     ans += ((n // 7 + 1) + (n // 7 + n % 7)) * (n % 7) // 2
        #     return ans
        
        ##### really doing it and add ####
        ans = 0
        cache = 0
        counter = 0
        while 1:
            if n == 0:
                return ans
            else:
                if counter == 7:
                    cache -= 6
                    counter = 0
                cache += 1
                counter += 1
                ans += cache
                n -= 1