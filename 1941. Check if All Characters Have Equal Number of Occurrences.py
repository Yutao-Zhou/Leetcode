class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ck = []
        c = []
        for i in s:
            if i in ck:
                pass
            else:
                ck.append(i)
                c.append(s.count(i))
        if c.count(c[0]) == len(c):
            return True
        else:
            return False