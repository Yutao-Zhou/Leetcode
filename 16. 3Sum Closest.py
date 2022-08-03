class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        nums = sorted(nums)
        closest = float('inf')
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                pass
            else:
                cache = [nums[0], nums[1], nums[2]]
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    cache = [nums[i],nums[l],nums[r]]
                    if nums[l] == nums[l - 1] and l - 1 != i:
                        l += 1
                    elif nums[i] + nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[i] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        return sum(cache)
                distance = abs(sum(cache) - target)
                if distance < closest:
                    ans = sum(cache)
                    closest = distance
        return ans