class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        #### Backtrack ####
        def buildNumber(n, number):
            if n == 0:
                ans.add(int(number))
                return
            digit = int(number[-1])
            if digit - k >= 0:
                buildNumber(n - 1, number + str(digit - k))
            if digit + k <= 9:
                buildNumber(n - 1, number + str(digit + k))
        
        ans = set()
        for i in range(1, 10):
            buildNumber(n - 1, str(i))
        return list(ans)