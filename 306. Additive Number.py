class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        #### Backtrack ####
        def build(start, last_one, last_two):
            if start == len(num):
                nonlocal ans
                ans = True
                return True
            

            if num[start] == "0":
                if last_one + last_two == 0:
                    if build(start + 1, 0, last_one):
                        return True
            else:
                for i in range(start + 1, len(num) + 1):
                    if last_one + last_two == int(num[start : i]):
                        if build(i, int(num[start : i]), last_one):
                            return True
        ans = False
        for i in range(1, len(num)):
            if len(str(int(num[:i]))) == len(num[:i]):
                for j in range(i + 1, len(num)):
                    if len(str(int(num[i : j]))) == len(num[i : j]):
                        build(j, int(num[i : j]), int(num[:i]))
        return ans