class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        #### frequency ####
        check1 = {}
        check2 = {}
        for i in words1:
            if i in check1:
                check1[i] += 1
            if i not in check1:
                check1[i] = 1
        for i in words2:
            if i in check2:
                check2[i] += 1
            if i not in check2:
                check2[i] = 1
       