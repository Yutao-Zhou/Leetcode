class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        #### Linear Count ####
        ans = [0, 0]
        for i in range(len(mat)):
            count = 0
            for n in mat[i]:
                if n == 1:
                    count += 1
            if count > ans[1]:
                ans[0] = i
                ans[1] = count
        return ans