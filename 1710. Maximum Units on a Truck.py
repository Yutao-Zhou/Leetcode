class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        i = 0
        j = 1
        k = 0
        counter = 0
        ans = 0
        for i in range(len(boxTypes)):
            for j in range(len(boxTypes)):
                if boxTypes[i][1] > boxTypes[j][1]:
                    boxTypes[i], boxTypes[j] = boxTypes[j], boxTypes[i]
        while k < len(boxTypes):
            if (counter + boxTypes[k][0]) > truckSize:
                ans += (truckSize - counter) * boxTypes[k][1]
                return ans
            elif (counter + boxTypes[k][0]) <= truckSize:
                ans += boxTypes[k][0] * boxTypes[k][1]
                counter += boxTypes[k][0]
            k += 1
        return ans