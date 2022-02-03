class Solution:
    def countTriples(self, n: int) -> int:
        #### n ** 3 ####
        # ans  = 0
        # i, j, k = 0, 0, 1
        # while i <= n:
        #     i += 1
        #     j = i
        #     while j <= n:
        #         j += 1
        #         k = j
        #         while k <= n:
        #             if i ** 2 + j ** 2 == k ** 2:
        #                 ans += 1
        #             k += 1
        # return ans * 2
        
        #### n ** 2 ####
        ans = 0
        check = []
        for i in range(n + 1):
            check.append(i ** 2)
        i, j = 0, 0
        for i in range(1,n + 1):
            for j in range(i + 1, n + 1):
                if i ** 2 + j ** 2 in check:
                    ans += 2
        return ans