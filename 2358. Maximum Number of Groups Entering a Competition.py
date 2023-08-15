class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        #### Greedy Math ####
        # n = len(grades)
        # ans = 0
        # while n > ans:
        #     ans += 1
        #     n -= ans
        # return ans

        #### binary search ####
        n = len(grades)
        l, r = 1, n
        while l < r:
            mid = (l + r + 1) // 2
            if mid * (mid + 1) / 2 > n:
                r = mid - 1
            else:
                l = mid
        return l