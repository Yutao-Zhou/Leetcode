class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ####### really doing it ######
        # drink = numBottles
        # drinkCache = 0
        # empty = numBottles
        # while numBottles >= numExchange:
        #     drinkCache = numBottles // numExchange
        #     drink += drinkCache
        #     empty = numBottles % numExchange 
        #     numBottles = drinkCache + empty
        # return drink
        
        ##### math #####
        return (numBottles * numExchange - 1) // (numExchange - 1)