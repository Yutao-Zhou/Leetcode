class Solution:
    def smallestNumber(self, pattern: str) -> str:
        #### Two Pointers ####
        lenPattern = len(pattern)
        ans = [str(i) for i in range(1, lenPattern + 2)]
        i, j = 0, 0
        while i < lenPattern and j < lenPattern:
            while j < lenPattern and pattern[j] != "D":
                j += 1
            i = j - 1
            while j < lenPattern and pattern[j] != "I":
                j += 1
            ans = ans[:i + 1] + ans[i + 1:j + 1][::-1] + ans[j + 1:]
            i = j + 1
            j = j + 1
        return "".join(ans)