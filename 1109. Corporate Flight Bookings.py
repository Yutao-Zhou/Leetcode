class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        #### distance line ####
        # ans = [0] * n
        # for i in bookings:
        #     for j in range(i[0] - 1,i[1]):
        #         ans[j] += i[2]
        # return ans
        
        seats = 0
        ans = [0] * n
        flight = []
        for i in bookings:
            flight.append((i[0],i[2]))
            flight.append((i[1] + 1,-i[2]))
        flight.sort()
        for i in range(len(flight) - 1):
            seats += flight[i][1]
            if flight[i][0] != flight[i + 1][0]:
                for i in range(flight[i][0] - 1,flight[i + 1][0] - 1):
                    ans[i] = seats
        return ans