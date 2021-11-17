class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while 1:
            if n % 2 == 0:
                ans += n / 2
                n = n / 2    
                print(n,ans)
            if n % 2 == 1:
                ans += (n - 1) / 2
                n = (n - 1) / 2 + 1
                print(n,ans)
            if n == 1:
                return int(ans)