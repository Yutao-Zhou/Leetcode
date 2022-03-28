class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        #### simulation ####
        ball = list(range(len(grid[0])))
        end = set()
        for level in grid:
            for i in range(len(ball)):
                if i not in end:
                    if level[ball[i]] == 1:
                        if ball[i] < len(level) - 1:
                            if level[ball[i] + 1] == -1:
                                ball[i] = -1
                                end.add(i)
                        if i not in end:
                            ball[i] += 1
                            if ball [i] >= len(level):
                                ball[i] = -1
                                end.add(i)
                    if level[ball[i]] == -1:
                        if 0 < ball[i]:
                            if level[ball[i] - 1] == 1:
                                ball[i] = -1
                                end.add(i)
                        if i not in end:
                            ball[i] -= 1
                            if ball[i] < 0:
                                ball[i] = -1
                                end.add(i)
        return ball