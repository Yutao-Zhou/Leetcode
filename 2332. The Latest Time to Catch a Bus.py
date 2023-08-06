class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        #### Pointer ####
        ans = 10 ** 9
        i = 0
        buses.sort()
        passengers.sort()
        num_buses = len(buses)
        num_passengers = len(passengers)
        
        for time in buses:
            seat = capacity
            while i < num_passengers and passengers[i] <= time and seat > 0:
                i += 1
                seat -= 1
        if seat == 0:
            ans = passengers[i - 1] - 1
        else:
            ans = buses[-1]

        while ans in set(passengers):
            ans -= 1
        return ans