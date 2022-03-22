class Solution:
    def decodeString(self, s: str) -> str:
        #### stack with start flag ####
        # stack = []
        # part = []
        # word = ""
        # number = []
        # ans = []
        # n = 0
        # start = False
        # for i in range(len(s)):
        #     if start == False:
        #         if "0" <= s[i] <= "9":
        #             start = True
        #             stack.append(s[i])
        #         else:
        #             ans.append(s[i])
        #     elif start == True:
        #         if s[i] == "]":
        #             while stack[-1] != "[":
        #                 part.append(stack.pop())
        #             part = part[::-1]
        #             part = "".join(part)
        #             stack.pop()
        #             while stack:
        #                 if "0" <= stack[-1] <= "9":
        #                     number.append(stack.pop())
        #                 else:
        #                     break
        #             number = number[::-1]
        #             n = int("".join(number))
        #             number = []
        #             for i in range(n):
        #                 word = word + part
        #             part = []
        #             if "[" in stack:
        #                 stack.append(word)
        #                 word = ""
        #             elif "[" not in stack:
        #                 ans.append(word)
        #                 word = ""
        #                 start = False
        #         else:
        #             stack.append(s[i])
        # return "".join(ans)
    
        #### smarter ####
        stack = []
        curNum = 0
        ans = ''
        for c in s:
            if c == '[':
                stack.append(ans)
                stack.append(curNum)
                ans = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                ans = prevString + num * ans
            elif c.isdigit():
                curNum = curNum * 10 + int(c)
            else:
                ans += c
        return ans