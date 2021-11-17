class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            ans = list(range(int(-n/2),int(n/2+1)))
            ans.remove(0)
            return ans
        if n % 2 != 0:
            ans = list(range(int(-(n-1)/2),int((n+1)/2)))
            return ans