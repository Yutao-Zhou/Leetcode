class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #### sort ####
        # s = list(s)
        # s.sort()
        # t = list(t)
        # t.sort()
        # for i in range(len(s)):
        #     if t[i] != s[i]:
        #         return t[i]
        # return t[-1]
        
        #### count frequency ####
        check = {}
        for num in s:
            if num in check:
                check[num] += 1
            if num not in check:
                check[num] = 1
        for num in t:
            if num not in check:
                return num
            if num in check:
                check[num] -= 1
                if check[num] < 0:
                    return num