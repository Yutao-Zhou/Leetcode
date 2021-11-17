class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x = []
        y = []
        for i in points:
            x.append(i[0])
            y.append(i[1])
        p = 1
        ans = 0
        ct = 0
        while p < len(x):
            xc = abs(x[p] - x[p-1])
            yc = abs(y[p] - y[p-1])
            while 1:
                if xc != 0 and yc != 0:
                    xc -= 1
                    yc -= 1
                    ct += 1
                elif xc != 0 and yc == 0:
                    xc -= 1
                    ct += 1
                elif yc != 0 and xc == 0:
                    yc -= 1
                    ct += 1
                elif xc == 0 and yc == 0:
                    ans = ct
                    p += 1
                    break
        return ans