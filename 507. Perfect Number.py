class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        #### brute force ####
        # res = 0
        # for i in range(1, num):
        #     if num % i == 0:
        #         res += i
        #         if res > num:
        #             return False
        # return res == num
        
        #### optimaled brute force ####
        if num == 1:
            return False
        res = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                res += i + num // i
                if res > num:
                    return False
        return res == num