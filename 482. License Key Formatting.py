class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        #### counter ####
        # counter = 0
        # s = s.split("-")
        # ans = []
        # s = "".join(s)[::-1]
        # for i in s:
        #     if counter == k:
        #         ans.append("-")
        #         counter = 0
        #     if ord("a") <= ord(i) <= ord("z"):
        #             ans.append(chr(ord(i) - 32))
        #             counter += 1
        #     else:
        #         ans.append(i)
        #         counter += 1
        # return "".join(ans)[::-1]
        
        #### string slice ####
        s = s.split("-")
        ans = []
        s = "".join(s)[::-1]
        s = s.upper()
        i = 0
        while i < len(s):
            ans.append(s[i:i + k])
            i += k
        return "-".join(ans)[::-1]