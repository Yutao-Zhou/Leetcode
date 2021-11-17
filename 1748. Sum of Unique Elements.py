class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = []
        d = []
        for i in nums:
            
            if i in ans:
                d.append(i)
            if i not in ans:
                ans.append(i)
        ans = list(set(ans) - set(d))
        return sum(ans)