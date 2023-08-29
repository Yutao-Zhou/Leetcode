class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # Brute force O(n ** 2)
        # ans = [0] * len(heights)
        # for i in range(len(heights) - 1):
        #     can_see = 0
        #     heighest = 0
        #     for j in range(i + 1, len(heights)):
        #         if heights[j] > heighest:
        #             can_see += 1
        #         heighest = max(heighest, heights[j])
        #         if heights[j] >= heights[i]:
        #             break
        #     ans[i] = can_see
        # return ans

        # Monotonic Stack
        stack = []
        ans = [0] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                ans[i] += 1
            if stack:
                ans[i] += 1
            stack.append(heights[i])
        return ans