class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        #### Brute Force Compare One By One ####
        # ans, l = 0, len(s)
        # for w in words:
        #     ans += 1
        #     lw = len(w)
        #     if lw > l:
        #         ans -= 1
        #         continue
        #     for i in range(lw):
        #         if w[i] != s[i]:
        #             ans -= 1
        #             break
        # return ans
    
        #### Brute Force Compare Directlly ####
        ans, l = 0, len(s)
        for w in words:
            ans += 1
            lw = len(w)
            if lw > l:
                ans -= 1
                continue
            if w != s[:lw]:
                ans -= 1
        return ans