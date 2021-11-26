class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##### dictionary ######
        # counter1 = {}
        # counter2 = {}
        # for i in s:
        #     if i in counter1:
        #         counter1[i] += 1
        #     if i not in counter1:
        #         counter1[i] = 1
        # for i in t:
        #     if i in counter2:
        #         counter2[i] += 1
        #     if i not in counter2:
        #         counter2[i] = 1
        # if counter1 == counter2:
        #     return True
        # else:
        #     return False
        
        ###### list sort #######
        # s = list(s)
        # t = list(t)
        # s.sort()
        # t.sort()
        # if s == t:
        #     return True
        # else:
        #     return False
        
        #### list sort one line#####
        return  s.sort() == t.sort()