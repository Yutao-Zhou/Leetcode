class Solution:
    def mySqrt(self, x: int) -> int:
        #### normal solve #####
        # i = 0
        # while 1:
        #     if i * i > x:
        #         return int(i) - 1
        #     else:
        #         i += 1
        
        ###### binary search #####
        l = 0
        h = x
        while l <= h:
            m = (h + l) // 2
            if m * m == x:
                return m
            if m * m > x and (m - 1) * (m - 1) < x:
                return m - 1
            if m * m < x:
                l = m + 1
            if m * m > x:
                h = m - 1