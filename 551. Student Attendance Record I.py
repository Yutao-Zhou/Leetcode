class Solution:
    def checkRecord(self, s: str) -> bool:
        #### Two counter ####
        # absentCounter = 0
        # lateCounter = 0
        # for string in s:
        #     if string == "A":
        #         absentCounter += 1
        #         lateCounter = 0
        #         if absentCounter > 1 or lateCounter == 3:
        #             return False
        #     if string == "L":
        #         lateCounter += 1
        #         if absentCounter > 1 or lateCounter == 3:
        #             return False
        #     else:
        #         lateCounter = 0
        # return True
        
        #### trick ####
        if s.count("A") > 1 or len(s.split("LLL")) > 1:
            return False
        else:
            return True