class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        #### simulation ####
        # ans = []
        # i = 1
        # while i <= n and target:
        #     if target[0] == i:
        #         ans.append("Push")
        #         target.pop(0)
        #         i += 1
        #     else:
        #         ans.append("Push")
        #         ans.append("Pop")
        #         i += 1
        # return ans
        
        #### math ####
        ans = []
        check = set(target)
        for i in range(1, target[-1] + 1):
            if i not in check:
                ans.append("Push")
                ans.append("Pop")
            else:
                ans.append("Push")
        return ans