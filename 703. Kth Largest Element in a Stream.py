class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse = True)[:k]
        self.k = k

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
            return val
        elif val < self.nums[-1] and len(self.nums) == self.k:
            return self.nums[-1]
        elif val > self.nums[0] and len(self.nums) == self.k:
            self.nums = [val] + self.nums[:-1]
            return self.nums[-1]
        else:
            for i in range(len(self.nums)):
                if self.nums[i] < val:
                    self.nums.insert(i, val)
                    break
            self.nums.append(val)
            self.nums = self.nums[:self.k]
            return self.nums[-1]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)