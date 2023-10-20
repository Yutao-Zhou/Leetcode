class Solution: 
    def countTriplets(self, arr: List[int]) -> int:
        pre_xor = [0] * len(arr)
        pre_xor[0] = arr[0]
        for i in range(1, len(arr)):
            pre_xor[i] = pre_xor[i - 1] ^ arr[i]

        ans = 0
        seen = {}
        for i in range(len(arr)):
            if i != 0 and pre_xor[i] == 0:
                ans += i
            if pre_xor[i] in seen:
                ans += (i - 1) * len(seen[pre_xor[i]]) - sum(seen[pre_xor[i]])
                seen[pre_xor[i]].append(i)
            else:
                seen[pre_xor[i]] = [i]
        return ans