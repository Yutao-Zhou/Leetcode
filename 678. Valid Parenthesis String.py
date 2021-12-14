class Solution:
    def checkValidString(self, s: str) -> bool:
        ####### stack ######
        # stack = []
        # for i in s:
        #     if i == "(" or i == "*":
        #         stack.append(i)
        #     if i == ")":
        #         if stack == []:
        #             return False
        #         else:
        #             for i in range(-1,-len(stack) - 1,-1):
        #                 if stack[i] == "(" or i == -len(stack):
        #                     stack.pop(i)
        #                     break
        # j = -2
        # if stack == []:
        #     return True
        # else:
        #     while j < -1 and j > -len(stack) - 1:
        #         if stack[-1] != "*":
        #             return False
        #         if stack[j] != "(":
        #             j -= 1
        #         elif stack[-1] == "*" and stack[j] == "(":
        #             stack.pop(j)
        #             stack.pop(-1)
        #             j = -2
        # return "(" not in stack
        
        ##### greedy #####
        minLeft = 0
        maxLeft = 0
        for i in s:
            if i == "(":
                minLeft += 1
            if i != "(":
                minLeft -= 1
            if i != ")":
                maxLeft += 1
            if i == ")":
                maxLeft -= 1
            if maxLeft < 0:
                return False
            minLeft = max(0,minLeft)
        return minLeft == 0