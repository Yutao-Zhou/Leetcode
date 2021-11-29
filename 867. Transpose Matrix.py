class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ##### doing it little by little #####
        # cache = []
        # ans = []
        # j = 0
        # while j < len(matrix[0]):
        #     for i in range(len(matrix)):
        #         cache.append(matrix[i][j])
        #     ans.append(cache)
        #     cache = []
        #     j += 1
        # return ans
        
        ###### zip not real solution ####
        return zip(*matrix)