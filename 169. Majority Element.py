class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ###### count frequency #####
        # frequency = {}
        # majority = 0
        # for i in nums:
        #     if i in frequency:
        #         frequency[i] += 1
        #     if i not in frequency:
        #         frequency[i] = 1
        # for i in frequency.items():
        #     if i[1] > len(nums) / 2:
        #         majority = i[0]
        # return majority
        
        ##### middle #####
        # nums.sort()
        # return nums[len(nums) // 2]
    
        ##### shorter loop, still count frequency #####
        # frequency = {}
        # for i in nums:
        #     if i not in frequency:
        #         frequency[i] = 0
        #     if i in frequency:
        #         frequency[i] += 1
        #         if frequency[i] > len(nums) / 2:
        #             return i
        
        ###### return max count, not a real solution ####
        freq = Counter(nums)
        val = max(freq.values())
        for i in freq:
            if freq[i] == val:
                return i