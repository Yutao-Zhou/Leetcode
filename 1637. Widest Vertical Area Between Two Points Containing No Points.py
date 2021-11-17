class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = []
        ans = 0
        points.sort()
        for i in points:
            x.append(i[0])
        for i in range(1,len(x)):
            if x[i] - x[i - 1] > ans:
                ans = x[i] - x[i - 1]
        return ans