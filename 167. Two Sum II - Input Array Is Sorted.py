class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #### two pointer with love ####
        # i = 0
        # j = len(numbers) - 1
        # while i < j:
        #     if numbers[i] + numbers[j] < target:
        #         i += 1
        #     if numbers[i] + numbers[j] > target:
        #         j -= 1
        #     if numbers[i] + numbers[j] == target:
        #         return [i + 1, j + 1]
        
        #### two pointer binary search ####
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1