class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        #### calculate distance ####
        out = []
        for circle in queries:
            ans = 0
            x = circle[0]
            y = circle[1]
            for point in points:
                d = abs(x - point[0]) ** 2 + abs(y - point[1]) ** 2
                if d <= circle[2] ** 2:
                    ans += 1
            out.append(ans)
        return out