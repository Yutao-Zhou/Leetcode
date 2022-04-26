class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        #### simulation no thinking ####
        # poisoned = set()
        # for time in timeSeries:
        #     for second in range(time, time + duration):
        #         poisoned.add(second)
        # return len(poisoned)
        
        #### with math ####
        ans = duration
        if len(timeSeries) == 0:
            return 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] < duration:
                ans += timeSeries[i] - timeSeries[i - 1]
            else:
                ans += duration
        return ans