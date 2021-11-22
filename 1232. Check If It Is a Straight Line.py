class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ##### slop #######
        counterx = 0
        countery = 0
        if len(coordinates) == 2:
            return True
        else:
            for i in range(0,len(coordinates)):
                if (coordinates[1][0] - coordinates[0][0]) != 0:
                    cach = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
                if (coordinates[1][0] - coordinates[0][0]) == 0:
                    cach = float('inf')              
                for i in range(2,len(coordinates)):
                    if (coordinates[i][0] - coordinates[i - 1][0]) == 0:
                        k = float('inf')
                    if (coordinates[i][0] - coordinates[i - 1][0]) != 0:
                        k = (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0])
                    if cach != k:
                        return False
                return True