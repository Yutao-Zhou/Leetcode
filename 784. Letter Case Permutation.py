class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        #### Backtrack ####
        # def backtrack(path, i):
        #     if len(path) == lenS:
        #         ans.append(path)
        #         return
        #     if s[i].isdigit():
        #         backtrack(path + s[i], i + 1)
        #     else:
        #         backtrack(path + s[i].lower(), i + 1)
        #         backtrack(path + s[i].upper(), i + 1)
        # lenS = len(s)
        # ans = []
        # backtrack("", 0)
        # return ans
        
        #### iteritive ####
        ans = [""]
        for i in range(len(s)):
            if s[i].isalpha():
                ans = [x + y for x in ans for y in {s[i].upper(), s[i].lower()}]
            else:
                ans = [x + s[i] for x in ans]
        return ans