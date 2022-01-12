class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        #### really doing it ####
        minDistance = 2 * 10 ** 4
        ans = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                distance = abs(points[i][0] - x) + abs(points[i][1] - y)
                if distance < minDistance:
                    minDistance = distance
                    ans = i
        return ans