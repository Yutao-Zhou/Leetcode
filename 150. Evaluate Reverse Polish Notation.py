class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #### stack one pass####
        stack = []
        for element in tokens:
            if 48 <= ord(element[0]) <= 57 or (element[0] == "-" and len(element) > 1):
                stack.append(element)
            else:
                if element == "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                if element == "-":
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(b - a)
                if element == "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                if element == "/":
                    a, b = int(stack.pop()), int(stack.pop())
                    stack.append(int(b / a))
        return stack[0]