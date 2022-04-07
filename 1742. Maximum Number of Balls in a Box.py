class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        #### simulation ####
        box = {}
        for n in range(lowLimit, highLimit + 1):
            boxNum = 0
            for char in str(n):
                boxNum += int(char)
            if boxNum in box:
                box[boxNum] += 1
            if boxNum not in box:
                box[boxNum] = 1
        return max(box.values())