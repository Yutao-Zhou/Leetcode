class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        #### Check one by one ####
        ans = [0, 0]
        even = 1
        while n:
            if even and n & 1:
                ans[0] +=1
            if not even and n & 1:
                ans[1] += 1
            even ^= 1
            n >>= 1
        return ans

        #### check by mask ####
        # return [(n & 0b10101010101).bit_count(), (n & 0b01010101010).bit_count()]