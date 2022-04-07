class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        #### simulation ####
        ans = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            ans += 1
        return ans