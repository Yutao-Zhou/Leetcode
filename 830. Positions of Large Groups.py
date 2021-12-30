class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        #### two pointer ####
        # i = 0
        # j = 1
        # ans = []
        # s += " "
        # while j < len(s):
        #     if s[j - 1] == s[j]:
        #         j += 1
        #     else:
        #         if j - i >= 3:
        #             ans.append([i,j - 1])
        #         i  = j
        #         j += 1
        # return ans
        
        #### another two pointer logic ####
        i = 0
        j = 0
        ans = []
        while i < len(s):
            while j < len(s) and s[j] == s[i]: 
                j += 1
            if j - i >= 3: 
                ans.append([i, j - 1])
            i = j
        return ans