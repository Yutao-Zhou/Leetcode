class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        for i in range(len(s)):
            if s[i] == ")" and stack == [] or s[i] == "]" and stack == [] or s[i] == "}" and stack == []:
                return False
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            if s[i] == ")":
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            if s[i] == "]":
                if stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            if s[i] == "}":
                if stack[-1] != "{":
                    return False
                else:
                    stack.pop()
        if stack != []:
            return False
        return True