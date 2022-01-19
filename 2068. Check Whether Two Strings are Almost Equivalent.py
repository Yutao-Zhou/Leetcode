class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        #### two hashmap and compare ####
        mapOne = {}
        mapTwo = {}
        for i in word1:
            if i in mapOne:
                mapOne[i] += 1
            elif i not in mapOne:
                mapOne[i] = 1
        for j in word2:
            if j in mapTwo:
                mapTwo[j] += 1
            elif j not in mapTwo:
                mapTwo[j] = 1
        for i in mapOne.items():
            if i[0] not in mapTwo:
                if i[1] > 3:
                    return False
            elif abs(i[1] - mapTwo[i[0]]) > 3:
                return False
        for i in mapTwo.items():
            if i[0] not in mapOne:
                if i[1] > 3:
                    return False
            elif abs(i[1] - mapOne[i[0]]) > 3:
                return False
        return True