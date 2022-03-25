class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #### linear counter ####
        # counter = 0
        # cache = []
        # ans = []
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         counter += 1
        #         if counter >= 0:
        #             cache.append(s[i])
        #         else:
        #             counter -= 1
        #     elif s[i] == ")":
        #         counter -= 1
        #         if counter >= 0:
        #             cache.append(s[i])
        #         else:
        #             counter += 1
        #     else:
        #         cache.append(s[i])
        # if counter == 0:
        #     return "".join(cache)
        # for i in range(-1, -len(cache) - 1, -1):
        #     if cache[i] == "(" and counter > 0:
        #         counter -= 1
        #         pass
        #     else:
        #         ans.append(cache[i])
        # return "".join(ans[::-1])
        
        #### stack ####
        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        for i in stack:
            s[i] = ""
        return "".join(s)