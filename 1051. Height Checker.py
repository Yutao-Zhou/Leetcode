class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #### fake sort solution ####
        # ans = 0
        # i = 0
        # check = sorted(heights)
        # while i < len(heights):
        #     if heights[i] != check[i]:
        #         ans += 1
        #     i += 1
        # return ans
        
        #### counting sort ####
        ans = 0
        a = 0
        sort = [0] * len(heights)
        counting = [0] * 101
        for i in heights:
            counting[i] += 1  
        for j in range(1,len(counting)):
            counting[j] += counting[j - 1]
        for k in heights:
               sort[counting[k] - 1] = k
               counting[k] -= 1
        while a < len(heights):
            if heights[a] != sort[a]:
                ans += 1
            a += 1
        return ans