class Solution:
    def sumOfMultiples(self, n: int) -> int:
        #### Jump ####
        # ans = 0
        # for i in range(1, n // 3 + 1):
        #     ans += 3 * i
        # for i in range(1, n // 5 + 1):
        #     if 5 * i % 3:
        #         ans += 5 * i
        # for i in range(1, n // 7 + 1):
        #     if 7 * i % 3 and 7 * i % 5:
        #         ans += 7 * i
        # return ans

        #### Brute Force ####
        ans = 0
        for i in range(1, n + 1):
            if not i % 3 or not i % 5 or not i % 7:
                ans += i
        return ans