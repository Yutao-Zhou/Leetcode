class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #### usage distance list ####
        # distanceLine = [0] * 1000
        # for i in trips:
        #     for j in range(i[1],i[2]):
        #         distanceLine[j] += i[0]
        # for i in distanceLine:
        #     if i > capacity:
        #         return False
        # return True
    
        #### check people on board ####
        onCar = []
        people = 0
        for i in trips:
            onCar.append((i[1],i[0]))
            onCar.append((i[2],-i[0]))
        onCar.sort()
        for i in onCar:
            people += i[1]
            if people > capacity:
                return False
        return True