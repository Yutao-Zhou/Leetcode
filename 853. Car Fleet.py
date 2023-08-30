class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #### Monotonic Stack ####
        stack = []
        time_map = {}
        for i in range(len(position)):
            time_map[position[i]] = (target - position[i]) / speed[i]
        position.sort()
        for car in position:
            while stack and time_map[stack[-1]] <= time_map[car]:
                stack.pop()
            stack.append(car)
        return len(stack)