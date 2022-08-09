class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        #### Brute Force try four direction ####
        if mat == target:
            return True
        n = len(mat)
        def rotate():
            rotated = []
            for i in range(n):
                cache = []
                for j in range(n):
                    cache.append(mat[j][i])
                rotated.append(cache[::-1])
            return rotated
        for i in range(3):
            mat = rotate()
            if mat == target:
                return True
        return False