class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #### string ####
        # ans = 0
        # for i in nums:
        #     if len(str(i)) % 2 == 0:
        #         ans += 1
        # return ans
        
        #### math digit ####
        ans = 0
        for i in nums:
            if i // (10 ** 5) != 0:
                ans += 1
            elif i // (10 ** 3) != 0 and i // (10 ** 4) == 0:
                ans += 1
            elif i // (10 ** 1) != 0 and i // (10 ** 2) == 0:
                ans += 1
        return ans