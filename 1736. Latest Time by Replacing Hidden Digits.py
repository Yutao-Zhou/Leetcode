class Solution:
    def maximumTime(self, time: str) -> str:
        #### brute force ####
        time = time.split(":")
        if time[0][0] == "?":
            if "4" <= time[0][1] <= "9":
                time[0] = "1" + time[0][1:]
            else:
                time[0] = "2" + time[0][1:]
        if time[0][1] == "?":
            if time[0][0] == "2":
                time[0] = time[0][:1] + "3"
            else:
                time[0] = time[0][:1] + "9"
        if time[1][0] == "?":
            time[1] = "5" + time[1][1:]
        if time[1][1] == "?":
            time[1] = time[1][:1] + "9"
        return ":".join(time)