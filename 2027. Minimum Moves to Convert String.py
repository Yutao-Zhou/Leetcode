class Solution:
    def minimumMoves(self, s: str) -> int:
        #### simulation and count, Greedy ####
        # s = list(s)
        # ans = 0
        # for i in range(len(s) - 2):
        #     if s[i] == "X":
        #         s[i] = "0"
        #         s[i + 1] = "0"
        #         s[i + 2] = "0"
        #         ans += 1
        # if "X" in s:
        #     ans += 1
        # return ans
        
        #### jump index, Greedy ####
        # ans = 0
        # i = 0
        # while i < len(s):
        #     if s[i] == "X":
        #         ans += 1
        #         i += 3
        #     else:
        #          i += 1
        # return ans
        
        #### find patern ####
        return subn('X.?.?', '', s)[1]