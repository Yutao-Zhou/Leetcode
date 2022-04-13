class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #### iteritive brute force ####
        # pre = "0"
        # n -= 1
        # while n:
        #     cur = ""
        #     for i in pre:
        #         if i == "0":
        #             cur = cur + "01"
        #         if i == "1":
        #             cur = cur + "10"
        #     pre = cur
        #     n -= 1
        # return pre[k - 1]
        
        #### k-th symbol ####
        res = 0
        while k > 1:
            if k % 2:
                k += 1 
            else:
                k = k // 2
            res ^= 1
        return res