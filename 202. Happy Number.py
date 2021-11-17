class Solution:
    def isHappy(self, n: int) -> bool:
        d = []
        ck = []
        while 1:
            if ck.count(n) == 2:
                return False
            n = str(n)
            for i in n:
                d.append(int(i))
            k = 0
            if int(n) == 1:
                return True
            else:
                for i in d:
                    k += i**2
                n = k
                ck.append(k)
                d = []