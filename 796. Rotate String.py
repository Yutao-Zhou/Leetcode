class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #### string slice and check ####
        # for i in range(len(s)):
        #     if (s[i:] + s[:i]) == goal:
        #         return True
        # return False
        
        #### check len and wither in double ####
        return goal in (s + s) and len(s) == len(goal)