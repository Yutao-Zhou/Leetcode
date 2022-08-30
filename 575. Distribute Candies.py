class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        #### Set ####
        return min(len(candyType) // 2, len(set(candyType)))
        
        #### Sort ####
        candyType.sort()
        ans = set()
        n = len(candyType) // 2
        for c in candyType:
            if n == 0:
                break
            if c not in ans:
                ans.add(c)
                n -= 1
        return len(ans)