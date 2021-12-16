class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        #### split and add ####
        # s = s.split(" ")
        # i = 0
        # ans = ""
        # while k != 0:
        #     ans += s[i] + " "
        #     i += 1
        #     k -= 1
        # return ans[:-1]
        
        #### join ####
        cache = []
        s = s.split(" ")
        i = 0
        while k != 0:
            cache.append(s[i])
            i += 1
            k -= 1
        return " ".join(cache)