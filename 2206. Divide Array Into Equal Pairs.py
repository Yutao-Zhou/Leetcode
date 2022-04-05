class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        #### hash map ####
        # m = {}
        # for n in nums:
        #     if n in m:
        #         m[n] += 1
        #     if n not in m:
        #         m[n] = 1
        # for value in m.values():
        #     if value % 2 != 0:
        #         return False
        # return True
        
        #### sort and check ####
        nums = sorted(nums)
        counter = 0
        pre = nums[0]
        for n in nums:
            if n == pre:
                counter += 1
            if n != pre:
                if counter % 2 != 0:
                    return False
                else:
                    pre = n
                    counter = 1
        return True