class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        #### Simulate ####
        time = 0
        while 1:
            time += 1
            if memory1 >= memory2 and memory1 >= time:
                memory1 -= time
            elif memory1 < memory2 and memory2 >= time:
                memory2 -= time
            else:
                break
        return [time, memory1, memory2]        