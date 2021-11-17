import math
class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for i in n:
            if int(i) > ans:
                ans = int(i)
        return ans