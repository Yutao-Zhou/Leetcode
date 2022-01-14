class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #### list map and recreat ####
        # ans = []
        # numsMap = [0] * 201
        # for i in nums:
        #     numsMap[i + 100] += 1
        # if len(nums) == len(set(nums)):
        #     return sorted(nums,reverse = True)
        # while max(numsMap) != 0:
        #     ans += [numsMap.index(max(numsMap)) - 100] * max(numsMap)
        #     numsMap[numsMap.index(max(numsMap))] = 0
        # return ans[::-1]
        
        #### counter and sort ####
        return sorted(nums, key = lambda x: (collections.Counter(nums)[x], -x))