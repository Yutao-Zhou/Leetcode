class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        #### Linear Scane ####
        # ans = []
        # for n in nums:
        #     for c in str(n):
        #         ans.append(int(c))
        # return ans

        #### Linear Scane Modular ####
        ans = []
        for n in nums:
            current = []
            while n > 0:
                current.append(n%10)
                n //= 10
            ans.extend(current[::-1])
        return ans