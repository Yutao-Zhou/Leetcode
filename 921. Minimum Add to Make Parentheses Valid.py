class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # l = 0
        # r = 0
        # ans = 0
        # for i in s:
        #     if i == "(":
        #         l += 1
        #     if i == ")":
        #         r += 1
        #     if r > l:
        #         ans += 1
        #         l = 0
        #         r = 0
        # if l > r:
        #     ans += l - r
        # return ans
        stack = []
        for i in range(0,len(s)):
            if stack == []:
                stack.append(s[i])
            elif s[i] == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) 