class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #### greedy iteritive two pointers ####
        # i = 0
        # j = 0
        # ans = 0
        # g = sorted(g)
        # s = sorted(s)
        # while i < len(g) and j < len(s):
        #     if g[i] <= s[j]:
        #         ans += 1
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
        # return ans
    
        #### greedy recursive ####
        g = sorted(g)
        s = sorted(s)
        def recursion(g, s, ans):
            if not g or not s:
                return ans
            if g[0] <= s[0]:
                return recursion(g[1:], s[1:], ans + 1)
            else:
                return recursion(g, s[1:], ans)
        return recursion(g, s, 0)