class Solution:
    def reverseWords(self, s: str) -> str:
        #### split invert and join ####
        # s = s.split(" ")
        # cache = []
        # ans = []
        # for i in s:
        #     for j in range(-1,-len(i) - 1,-1):
        #         cache.append(i[j])
        #     ans.append("".join(cache))
        #     cache = []
        # ans = " ".join(ans)
        # return ans
        
        #### two pointer ####
        i = 0
        j = 1
        cache = ""
        ans = ""
        s += " "
        while 1:
            if j >= len(s):
                return ans[:-1]
            if s[j] == " ":
                cache = s[i:j][::-1]
                ans += cache + " "
                cache = []
                i = j + 1
                j += 1
            j += 1