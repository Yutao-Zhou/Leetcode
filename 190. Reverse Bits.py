class Solution:
    def reverseBits(self, n: int) -> int:
        #### Standard ####
        ans = 0
        for i in range(32):
            ans += n & 1
            ans <<= 1
            n >>= 1
        return ans >> 1

        #### Compact ####
        ans = 0
        for i in range(32):
            ans =  ans << 1 + n & 1
            n >>= 1
        return ans