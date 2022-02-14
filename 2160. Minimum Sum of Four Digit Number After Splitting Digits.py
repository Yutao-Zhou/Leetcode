class Solution:
    def minimumSum(self, num: int) -> int:
        #### find minimum digit and calculate ####
        num = sorted(str(num))
        return(int(num[0]) + int(num[1])) * 10 + int(num[2]) + int(num[3])