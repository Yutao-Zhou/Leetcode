class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        #### Brute Force check every pair ####
        nums.sort()
        ans, l, seen = 0, len(nums), set()
        for i in range(l - 1):
            for j in range(i + 1, l):
                if nums[j] - nums[i] == k and (nums[i], nums[j]) not in seen:
                    ans += 1
                    seen.add((nums[i], nums[j]))
                if nums[j] - nums[i] >= k:
                    break
        return ans