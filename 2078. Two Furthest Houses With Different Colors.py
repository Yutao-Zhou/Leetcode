class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        #### O(n ** 2) ####
        # ans = 0
        # for i in range(len(colors)):
        #     for j in range(i,len(colors)):
        #         if colors[i] != colors[j] and j - i > ans:
        #             ans = j - i
        # return ans
        
        #### start from both end ####
        if colors[0] != colors[-1]:
            return len(colors) - 1
        ans = []
        for i in range(len(colors)):
            if colors[i] != colors[-1]:
                ans.append(len(colors) - i - 1)
        for j in range(-1,-len(colors),-1):
            if colors[j] != colors[0]:
                ans.append(j - -len(colors))
        return max(ans)