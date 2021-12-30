class Solution:
    def getLucky(self, s: str, k: int) -> int:
        #### step by step with no thinking ####
        cache = 0
        s = list(s)
        for i in range(len(s)):
            s[i] = str(ord(s[i]) - 96)
        s = "".join(s)
        while k > 0:
            for i in s:
                cache += int(i)
            s = str(cache)
            k -= 1
            cache = 0
        return s