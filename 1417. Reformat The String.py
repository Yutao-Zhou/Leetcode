class Solution:
    def reformat(self, s: str) -> str:
        l = []
        n = []
        j = 0
        for i in s:
            try: 
                int(i)
                n.append(str(i))
            except:
                l.append(i)
        if len(l) == len(n) + 1:
            for i in l:
                n.insert(j,i)
                j += 2
            return "".join(n)
        if len(l) == len(n) - 1 or len(l) == len(n):
            for i in n:
                l.insert(j,i)
                j += 2
            return "".join(l)
        else:
            return ""