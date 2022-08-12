class Solution:
    def calculate(self, s: str) -> int:
        #### stack ####
        stack = []
        currentNumber = ""
        currentOperation = ""
        for c in s:
            if c == " ":
                pass
            elif 48 <= ord(c) <= 57:
                currentNumber = currentNumber + c
            else:
                stack.append(int(currentNumber))
                currentNumber = ""
                if currentOperation == "*":
                    n = stack.pop() * stack.pop()
                    stack.append(n)
                    currentOperation = ""
                if currentOperation == "/":
                    n2 = stack.pop()
                    n1 = stack.pop()
                    stack.append(int(n1 / n2))
                    currentOperation = ""
                if c == "-":
                    currentNumber = currentNumber + "-"
                if c == "*" or c == "/":
                    currentOperation = c
        stack.append(int(currentNumber))
        if currentOperation == "*":
            n = stack.pop() * stack.pop()
            stack.append(n)
        if currentOperation == "/":
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(int(n1 / n2))
        return sum(stack)