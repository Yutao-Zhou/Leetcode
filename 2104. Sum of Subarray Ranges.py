class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # Brute force
        # ans = 0
        # for i in range(len(nums)):
        #     largest = nums[i]
        #     smallest = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         largest = max(largest, nums[j])
        #         smallest = min(smallest, nums[j])
        #         ans += largest - smallest
        # return ans

        # Monotonic Stack
        # ans = 0
        # stack = [(nums[0], 0)]
        # nums.append(float(inf))
        # for i in range(1, len(nums)):
        #     while stack and nums[i] >= stack[-1][0]:
        #         value, index = stack.pop()
        #         if stack:
        #             left_index = stack[-1][1]
        #         else:
        #             left_index = -1
        #         ans += (i - index) * (index - left_index) * value
        #     stack.append((nums[i], i))
        # stack = [(nums[0], 0)]
        # nums[-1] = float(-inf)
        # for i in range(1, len(nums)):
        #     while stack and nums[i] <= stack[-1][0]:
        #         value, index = stack.pop()
        #         if stack:
        #             left_index = stack[-1][1]
        #         else:
        #             left_index = -1
        #         ans -= (i - index) * (index - left_index) * value
        #     stack.append((nums[i], i))
        # return ans

        # Monotonic Stack Space Optimal
        ans = 0
        stack = []
        nums.append(float(inf))
        for i in range(len(nums)):
            while stack and nums[i] >= nums[stack[-1]]:
                index = stack.pop()
                if stack:
                    left_index = stack[-1]
                else:
                    left_index = -1
                ans += (i - index) * (index - left_index) * nums[index]
            stack.append(i)
        stack = []
        nums[-1] = float(-inf)
        for i in range(len(nums)):
            while stack and nums[i] <= nums[stack[-1]]:
                index = stack.pop()
                if stack:
                    left_index = stack[-1]
                else:
                    left_index = -1
                ans -= (i - index) * (index - left_index) * nums[index]
            stack.append(i)
        return ans