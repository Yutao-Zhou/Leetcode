class Solution:
    def maxDepth(self, s: str) -> int:
        #### stack and max deep ###
        # ans = 0
        # stack = []
        # for i in s:
        #     if i == "(":
        #         stack.append(i)
        #     if len(stack) > ans:
        #         ans = len(stack)
        #     if i == ")" and stack:
        #         stack.pop()
        # return ans
        
        #### only save max ####
        cache = 0
        ans = 0
        for i in s:
            if i == "(":
                cache += 1
            if cache > ans:
                ans = cache
            if i == ")":
                cache -= 1
        return ans