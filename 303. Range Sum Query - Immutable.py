class NumArray:

    def __init__(self, nums: List[int]):
        self.left_sum = [0]
        for i in range(0, len(nums)):
            self.left_sum.append(self.left_sum[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.left_sum[right + 1] - self.left_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)