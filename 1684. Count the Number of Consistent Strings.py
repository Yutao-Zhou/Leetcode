class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d  = []
        ans = 0
        for i in allowed:
            d.append(i)
        for i in words:
            c = 0
            for j in i:
                if j in d:
                    print(j)
                    c += 1
                    if c == len(i):
                        ans += 1
                else:
                    break
        return ans