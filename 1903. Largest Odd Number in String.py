class Solution:
    def largestOddNumber(self, num: str) -> str:
        # num = list(num)
        # i = -1
        # while 1:
        #     if i == -len(num) - 1:
        #         break
        #     if int(num[i]) % 2 == 0:
        #         num.pop()
        #     else:
        #         return "".join(num)
        # return ""
        
        for i in range(len(num) - 1, -1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""