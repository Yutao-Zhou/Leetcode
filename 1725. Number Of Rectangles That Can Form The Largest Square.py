class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        #### append shorter side and count, faster more RAM ####
        # shorter = []
        # ans = 0
        # for i in rectangles:
        #     shorter.append(min(i))
        # target = max(shorter)
        # for i in shorter:
        #     if i == target:
        #         ans += 1
        # return ans
    
        #### less RAM, Slower ####
        ans = 0
        target = 0
        for i in rectangles:
            if min(i) > target:
                target = min(i)
                ans = 0
            if target == min(i):
                ans += 1
        return ans