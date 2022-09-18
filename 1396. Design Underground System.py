class UndergroundSystem:

    def __init__(self):
        self.station = {}
        self.customer = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = (stationName, t)
        if stationName not in self.station:
            self.station[stationName] = {}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if stationName not in self.station[self.customer[id][0]]:
            self.station[self.customer[id][0]][stationName] = [t - self.customer[id][1], 1]
        else:
            self.station[self.customer[id][0]][stationName][0] += t - self.customer[id][1]
            self.station[self.customer[id][0]][stationName][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station[startStation][endStation][0] / self.station[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)