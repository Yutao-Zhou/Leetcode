class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        cach = 0
        res = []
        for i in nums:
            cach += i
            if cach < 0:
                res.append(cach)
        if res == []:
            return 1
        else:
            return abs(min(res)) + 1