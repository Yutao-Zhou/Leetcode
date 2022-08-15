class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #### Sort and Eliminate ####
        l = len(points)
        i, j, ans = 0, 1, 1
        points.sort(key = lambda y:y[0])
        left, right = points[0][0], points[0][1]
        while j < l:
            if points[j][0] <= right and points[j][1] >= left:
                left, right = max(left, points[j][0]), min(right, points[j][1])
            else:
                ans += 1
                i = j
                left, right = points[i][0], points[i][1]
            j += 1
        return ans