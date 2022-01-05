class Solution:
    def checkString(self, s: str) -> bool:
        #### hard solve ####
        # appear = False
        # for i in s:
        #     if i == "b":
        #         appear = True
        #     if i == "a" and appear:
        #         return False
        # return True
        
        #### sort ####
        # check = list(s)
        # check.sort()
        # check = "".join(check)
        # return check == s
        
        #### find pattern ####
        return "ba" not in s