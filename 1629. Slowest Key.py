class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        #### one pass check ####
        cache = releaseTimes[0]
        index = 0
        for i in range(1,len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i - 1] == cache and keysPressed[i] > keysPressed[index]:
                index = i
            if releaseTimes[i] - releaseTimes[i - 1] > cache:
                index = i
                cache = releaseTimes[i] - releaseTimes[i - 1]
        return keysPressed[index]