class Solution:
    def countPrimes(self, n: int) -> int:
        #### Brute Force ####
        # ans = 0
        # for i in range(2, n):
        #     end = int(i ** 0.5)
        #     prime = True
        #     for j in range(2, end + 1):
        #         if i % j == 0:
        #             prime = False
        #             break
        #     if prime:
        #         ans += 1
        # return ans
        
        #### Sieve of Eratosthenes ####
        if n < 3:
            return 0
        prime = [True] * n
        prime[0] = False
        prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                prime[i * i: n: i] = [False] * len(prime[i * i: n: i])
        return sum(prime)