class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        #### string index of first non-zero ####
        # if num == 0:
        #     return True
        # num = str(num)
        # return num[-1] != "0"
        
        #### pure math ####
        # if num == 0:
        #     return True
        # return num % 10 != 0
        
        #### one linear ####
        # return num % 10 != 0 or num == 0
        
        #### simulation ####
        def reverseNum(num):
            i = 0
            reverse = 0
            while 1:
                reverse = reverse * 10 + (num % (10 ** i)) // (10 ** (i - 1))
                if num % (10 ** i) == num:
                    return int(reverse)
                i += 1
        return reverseNum(reverseNum(num)) == num