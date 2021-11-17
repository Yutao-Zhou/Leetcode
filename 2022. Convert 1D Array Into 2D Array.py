class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = [[] for k in range(m)]
        j = 0
        i = 0
        if m*n == len(original):
            while 1:
                if i < len(original):
                    ans[j].append(original[i])
                    i += 1
                    if i % n == 0:
                        j += 1
                else:
                    return ans
        else:
            return []