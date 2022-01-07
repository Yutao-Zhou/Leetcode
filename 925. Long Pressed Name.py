class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        #### bad two pointer ####
        # i, j = 0, 0
        # if name[0] != typed[0]:
        #     return False
        # while i < len(name) and j < len(typed):
        #     if name[i] != typed[j]:
        #         if typed[j] != typed[j - 1]:
        #             return False
        #         j += 1
        #     else:
        #         i += 1
        #         j += 1
        # if i == len(name):
        #     for i in range(j,len(typed)):
        #         if typed[j - 1] != typed[i]:
        #             return False
        #     return True
        # return False
        
        #### better two pointer ####
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)