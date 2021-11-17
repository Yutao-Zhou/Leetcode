class Solution:
    def frequencySort(self, s: str) -> str:
        ck = {}
        ans = []
        for i in s:
            if i not in ck:
                ck[i] = 0
            if i in ck:
                ck[i] += 1
        ck = sorted(ck.items(), key=lambda item: item[1])
        for i in ck:
            ans.append(i[0]*i[1])
        ans = "".join(ans)[::-1]
        return ans