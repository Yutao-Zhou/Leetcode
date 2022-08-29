class Solution:
    #### random swap (Fisher-Yates Algorithm) ####
    def __init__(self, nums: List[int]):
        import random 
        self.nums = nums
        self.l = len(nums)
        self.original = nums[:]

    def reset(self) -> List[int]:
        self.nums = self.original[:]
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(self.l):
            r = randint(0, self.l - 1)
            self.nums[i], self.nums[r] = self.nums[r], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()