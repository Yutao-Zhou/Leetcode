class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        #### Loop ####
        # hit = 0
        # counter = 0
        # for l in s:
        #     if l == letter:
        #         hit += 1
        #     counter += 1
        # return hit * 100 // counter
        
        #### Buildin ####
        return s.count(letter) * 100 // len(s)