class Solution:
    def reformatDate(self, date: str) -> str:
        #### split ####
        # date = date.split(" ")
        # month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        # if len(date[0]) == 3:
        #     ans = date[2] + "-" + month[date[1]] + "-" + "0" + date[0][:-2]
        # else:
        #     ans = date[2] + "-" + month[date[1]] + "-" + date[0][:-2]
        # return ans
        
        #### read slice ####
        month = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        if len(date) == 12:
            date = "0" + date
        ans = date[-4:] + "-" + month[date[5:8]] + "-" + date[0:2]
        return ans