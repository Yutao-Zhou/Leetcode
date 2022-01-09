class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #### simulation ####
        # Two situation that robot can loop
        # 1. Robot returned to original
        # 2. Robot changed direction
        # direction = 0
        # x = 0
        # y = 0
        # for i in instructions:
        #     if i == "L":
        #         if direction == 0:
        #             direction = 3
        #         else:
        #             direction -= 1
        #     if i == "R":
        #         if direction == 3:
        #             direction = 0
        #         else:
        #             direction += 1
        #     if i == "G":
        #         if direction == 0:
        #             y += 1
        #         if direction == 1:
        #             x += 1
        #         if direction == 2:
        #             y -= 1
        #         if direction == 3:
        #             x -= 1
        # if (x == 0 and y == 0) or direction != 0:
        #     return True
        # return False
        
        #### repeat four times and check ####
        # if end up left or right repeat in four loop
        # if end up down repeat in two loop
        instructions += instructions
        instructions += instructions
        direction = 0
        x = 0
        y = 0
        for i in instructions:
            if i == "L":
                if direction == 0:
                    direction = 3
                else:
                    direction -= 1
            if i == "R":
                if direction == 3:
                    direction = 0
                else:
                    direction += 1
            if i == "G":
                if direction == 0:
                    y += 1
                if direction == 1:
                    x += 1
                if direction == 2:
                    y -= 1
                if direction == 3:
                    x -= 1
        return x == 0 and y == 0