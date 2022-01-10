class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #### map and creat ####
        # ans = ""
        # sdic = {}
        # for i in s:
        #     if i in sdic:
        #         sdic[i] += 1
        #     if i not in sdic:
        #         sdic[i] = 1
        # for i in order:
        #     if i in sdic:
        #         ans += i * sdic[i]
        #         del sdic[i]
        # for i in sdic.items():
        #     ans += i[0] * i[1]
        # return ans
        
        #### bubble sort ####
        i, j = 0, 1
        s = list(s)
        check = set(s)
        for k in order:
            if k in check:
                while j < len(s):
                    if s[i] == k:
                        i += 1
                    elif s[j] == k:
                        s[i], s[j] = s[j], s[i]
                        i += 1
                    j += 1
                j = i + 1
        return "".join(s)