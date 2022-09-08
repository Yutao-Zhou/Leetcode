class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #### Backtrack from subsets ####
        sumOfNums = sum(nums)
        lNums = len(nums)
        if sumOfNums % k:
            return False
        targetSum = sumOfNums // k
        visited = [False] * lNums
        nums.sort(reverse = True)
        memo = []
        def backtrack(currentSum, position, remainK):
            if remainK == 1:
                return True
            if currentSum == targetSum:
                memo.append(visited)
                return backtrack(0, 0, remainK - 1)
            for i in range(position, lNums):
                if not visited[i] and currentSum + nums[i] <= targetSum:
                    visited[i] = True
                    if backtrack(currentSum + nums[i], i + 1, remainK):
                        return True
                    visited[i] = False
            return False
        return backtrack(0, 0, k)