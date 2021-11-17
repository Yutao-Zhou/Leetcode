class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        cache = []
        ans = []
        r = 0
        while 1:
            r += 1
            if r == numRows + 1:
                return ans
            elif r == 1:
                ans = [[1]]
            elif r == 2:
                ans = [[1],[1,1]]
                cache = [1,1]
            else:
                sans = [1]
                for i in range(len(cache)-1):
                    c = cache[i] + cache[i+1]
                    sans.append(c)
                sans.append(1)
                ans.append(sans)
                cache = sans