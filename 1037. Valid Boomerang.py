class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        #### calculate slope ####
        i = 0
        j = 1
        s = []
        while i < len(points) - 1:
            if points[j][0] == points[i][0]:
                s.append(float('inf'))
                j += 1
                if j == len(points):
                    i += 1
                    j = i + 1
            else:
                slope =  (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                s.append(slope)
                j += 1
                if j == len(points):
                    i += 1
                    j = i + 1
        return len(set(s)) == len(s)