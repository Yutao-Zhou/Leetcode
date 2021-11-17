class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l = {}
        lt = {}
        if len(word1) != len(word2):
            return False
        else:
            for i in word1:
                if i not in l:
                    l[i] = 1
                elif i in l:
                    l[i] += 1
            for i in word2:
                if i not in lt:
                    lt[i] = 1
                elif i in lt:
                    lt[i] += 1
            if sorted(l.values()) != sorted(lt.values()):
                return False
            if sorted(l) != sorted(lt):
                return False
            return True