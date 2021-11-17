class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = []
        d = []
        for i in paths:
            s.append(i[0])
            d.append(i[1])
        for j in d:
            if j in s:
                pass
            else:
                return j