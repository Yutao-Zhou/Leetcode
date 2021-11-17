class Solution:
    def thousandSeparator(self, n: int) -> str:
        # ans = []
        # n = str(n)
        # for i in range(-1,-len(n) - 1,-1):
        #     if i % 3 == 0 and i != -len(n):
        #         ans.insert(0,n[i])
        #         ans.insert(0,".")
        #     else:
        #         ans.insert(0,n[i])
        # return "".join(ans)
        
        return f"{n:,}".replace(",",".")