class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        #### Stack ####
#         def checkStack(b, a, point):
#             nonlocal stack, ans
#             numsA = 0
#             while stack:
#                 if stack[-1] == a:
#                     numsA += 1
#                 elif numsA > 0:
#                     ans += point
#                     numsA -= 1
#                 stack.pop()
        
#         def iterrate(a, b, x, y):
#             nonlocal stack, ans, i
#             while i < len(s):
#                 if s[i] != a and s[i] != b:
#                     checkStack(b, a, y)
#                     stack = []
#                 elif s[i] == a:
#                     stack.append(a)
#                 elif s[i] == b:
#                     if stack and stack[-1] == a:
#                         stack.pop()
#                         ans += x
#                     else:
#                         stack.append(b)
#                 i += 1
#         stack = []
#         i, ans = 0, 0
#         if x >= y:
#             iterrate("a", "b", x, y)
#             checkStack("b", "a", y)
#         else:
#             iterrate("b", "a", y, x)
#             checkStack("a", "b", x)
#         return ans
        
        #### Improved Stack with Counter ####        
        def iterrate(a, b, x, y):
            i = 0
            while i < len(s):
                if s[i] != a and s[i] != b:
                    self.ans += min(self.numsA, self.numsB) * y
                    self.stack = []
                    self.numsA, self.numsB = 0, 0
                elif s[i] == a:
                    self.stack.append(a)
                    self.numsA += 1
                elif s[i] == b:
                    if self.stack and self.stack[-1] == a:
                        self.stack.pop()
                        self.ans += x
                        self.numsA -= 1
                    else:
                        self.stack.append(b)
                        self.numsB += 1
                i += 1
        self.stack = []
        self.ans = 0
        self.numsA, self.numsB = 0, 0
        if x >= y:
            iterrate("a", "b", x, y)
            self.ans += min(self.numsB, self.numsA)* y
        else:
            iterrate("b", "a", y, x)
            self.ans += min(self.numsA, self.numsB) * x
        return self.ans