class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        #### Count Bit ####
        ans = 0
        bit_map = [0] * 31
        for n in nums:
            counter = -1
            while n:
                if n & 1:
                    bit_map[counter] += 1
                n >>= 1
                counter -= 1
        for i in range(-1, -len(bit_map) - 1, -1):
            if bit_map[i] >= k:
                ans += 2 ** (-i - 1)
        return ans