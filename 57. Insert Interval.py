class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #### Brute Force One Pass Extra List ####
        # ans = []
        # for i in range(len(intervals)):
        #     if intervals[i][1] < newInterval[0]:
        #         ans.append(intervals[i])
        #     elif  intervals[i][0]  > newInterval[1]:
        #         ans.append(newInterval)
        #         newInterval = []
        #         ans += intervals[i:]
        #         break
        #     else:
        #         newInterval[0] = min(intervals[i][0], newInterval[0])
        #         newInterval[1] = max(intervals[i][1], newInterval[1])
        # if newInterval:
        #     ans.append(newInterval)
        # return ans
        
        #### Inplace ####
        i = 0
        while i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                i += 1
            elif intervals[i][0]  > newInterval[1]:
                intervals.insert(i, newInterval)
                newInterval = []
                break
            else:
                node = intervals.pop(i)
                newInterval[0] = min(node[0], newInterval[0])
                newInterval[1] = max(node[1], newInterval[1])
        if newInterval:
            intervals.append(newInterval)
        return intervals