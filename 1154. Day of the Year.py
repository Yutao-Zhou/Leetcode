class Solution:
    def dayOfYear(self, date: str) -> int:
        #### unnecessary dictionary ####
        # ans = 0
        # m = 1
        # months = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        # date = date.split("-")
        # for i in range(len(date)):
        #     date[i] = int(date[i])
        # if date[0] % 4 == 0 and date[0] != 1900:
        #     months[2] = 29
        # else:
        #     months[2] = 28
        # while m < date[1]:
        #     print(months[m])
        #     ans += months[m]
        #     m += 1
        # ans += date[2]
        # return ans
        
        #### datetime cheat ####
        # date = date.split("-")
        # for i in range(len(date)):
        #     date[i] = int(date[i])
        # return int((datetime.datetime(date[0], date[1], date[2]) - datetime.datetime(date[0], 1, 1)).days + 1)
        
        #### list ####
        ans = 0
        m = 0
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        date = date.split("-")
        for i in range(len(date)):
            date[i] = int(date[i])
        if date[0] % 4 == 0 and date[0] != 1900:
            months[1] = 29
        while m < date[1] - 1:
            ans += months[m]
            m += 1
        ans += date[2]
        return ans