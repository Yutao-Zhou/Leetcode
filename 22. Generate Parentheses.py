class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack (s, l, r):
            if len(s) == 2*n:
                ans.append(s)
                return
            if r < l:
                return
            if l > 0:
                backtrack(s + "(", l - 1, r)
            if r > 0:
                backtrack(s + ")", l, r - 1)
        backtrack("", n, n)
        return ans