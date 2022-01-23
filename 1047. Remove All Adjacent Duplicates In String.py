class Solution:
    def removeDuplicates(self, s: str) -> str:
        #### fundamental stack ####
        stack = []
        for i in s:
            if stack == []:
                stack.append(i)
            elif i == stack[-1]:
                stack.pop()
            elif i != stack[-1]:
                stack.append(i)
        return "".join(stack)