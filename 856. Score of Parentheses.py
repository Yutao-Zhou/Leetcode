class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        #### Stack with score ####
        # stack = [0]
        # for c in s:
        #     if c == ")":
        #         current = stack.pop()
        #         stack[-1] += max(1, current * 2)
        #     else:
        #         stack.append(0)
        # return stack[-1]

        #### Calculation ####
        ans, deepth = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                deepth += 1
            else:
                deepth -= 1
                if s[i - 1] == "(":
                    ans += 1 << deepth
        return ans