class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ")":
                cache = ""
                while stack:
                    current = stack.pop()
                    if current == "(":
                        stack.append(cache[::-1])
                        break
                    else:
                        cache = current + cache
            else:
                stack.append(c)
        return "".join(stack)