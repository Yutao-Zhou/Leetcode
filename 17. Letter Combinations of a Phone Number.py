class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #### Recursion ####
        l, ans = len(digits), []
        if l == 0:
            return ans
        L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        def backtrack(start, current):
            if len(current) == l:
                ans.append(current)
                return
            for i in range(0, len(L[digits[start]])):
                backtrack(start + 1, current + L[digits[start]][i])
        backtrack(0, "")
        return ans