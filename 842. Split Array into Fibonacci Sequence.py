class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        #### Backtrack ####
        def splitNumber(start, path):
            if start == len(num):
                if len(path) > 2:
                    nonlocal ans
                    ans = path
                return
            
            if num[start] == '0' and ((len(path) >= 2 and path[-2] + path[-1] == 0) or len(path) < 2):
                splitNumber(start + 1, path + [0])
            else:
                for d in range(start, len(num)):
                    if int(num[start : d + 1]) >= 2 ** 31:
                        break
                    if len(path) >= 2 and path[-2] + path[-1] != int(num[start : d + 1]):
                        continue
                    splitNumber(d + 1, path + [int(num[start : d + 1])])

        ans = []
        splitNumber(0, [])
        return ans