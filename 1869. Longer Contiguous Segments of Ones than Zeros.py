class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        #### try to be smarter ####
        # longestOne = 0
        # longestZero = 0
        # one = 0
        # zero = 0
        # if s == "1":
        #     return True
        # if s[-1] == "0":
        #     s += "1"
        # else:
        #     s += "0"
        # for i in s:
        #     if i == "1":
        #         one += 1
        #         if zero > longestZero:
        #             longestZero = zero
        #         zero = 0
        #     if i == "0":
        #         zero += 1
        #         if one > longestOne:
        #             longestOne = one
        #         one = 0
        # return longestOne > longestZero
        
        #### concise code version(see wither need to update longest everytime) ####
        # longestOne = 0
        # longestZero = 0
        # one = 0
        # zero = 0
        # for i in s:
        #     if i == "1":
        #         zero = 0
        #         one += 1
        #         if one > longestOne:
        #             longestOne = one
        #         zero = 0
        #     if i == "0":
        #         one = 0
        #         zero += 1
        #         if zero > longestZero:
        #             longestZero = zero
        # return longestOne > longestZero
        
        #### split compare length ####
        sZero = s.split('1')
        sOne = s.split('0')
        longestOne = 0
        longestZero = 0
        for zeros in sZero:
            if len(zeros) > longestZero:
                longestZero = len(zeros)
        for ones in sOne:
            if len(ones) > longestOne:
                longestOne = len(ones)
        return longestOne > longestZero