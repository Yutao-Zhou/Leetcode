class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = -1
        high = len(nums) - 1
        while high - 1 >= low:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1