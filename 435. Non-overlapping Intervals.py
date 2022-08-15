class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #### Sort Greedy ####
        l = len(intervals)
        if l == 1:
            return 0
        ans, i, j = 0, 0, 1
        intervals.sort(key=lambda y: y[0])
        while j < l:
            if intervals[j][0] >= intervals[i][1]:
                i = j
                j += 1
            else:
                ans += 1
                if intervals[i][1] <= intervals[j][1]:
                    j += 1
                else:
                    i = j
                    j += 1
        return ans