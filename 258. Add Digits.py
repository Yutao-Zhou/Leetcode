class Solution:
    def addDigits(self, num: int) -> int:
        ##### really doing it ####
        # cache = 0
        # while num > 9:
        #     while num != 0:
        #         cache += num % 10
        #         num = num // 10
        #     num = cache
        #     cache = 0
        # return num
        
        ##### math ######
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1