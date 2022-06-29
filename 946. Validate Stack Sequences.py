class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        #### normal stack ####
        # stack = []
        # while pushed:
        #     stack.append(pushed.pop(0))
        #     while stack and popped:
        #         if stack[-1] == popped[0]:
        #             stack.pop()
        #             popped = popped[1:]
        #         else:
        #             break
        # return not stack
        
        #### stack with pointers ####
        i, j = 0, 0
        stack = []
        while i < len(pushed):
            stack.append(pushed[i])
            i += 1
            while stack and j < len(popped):
                if stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    break
        return not stack