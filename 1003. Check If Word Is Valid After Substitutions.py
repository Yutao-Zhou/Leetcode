class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter == "a" or letter == "b":
                stack.append(letter)
            if letter == "c":
                if len(stack) >= 2:
                    if stack[-2] == "a" and stack[-1] == "b":
                        stack.pop()
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not stack