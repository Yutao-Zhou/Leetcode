class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        pre_xor = [0] * len(arr)
        pre_xor[0] = arr[0]
        for i in range(1, len(arr)):
            pre_xor[i] = pre_xor[i - 1] ^ arr[i]
        for query in queries:
            if query[0] == 0:
                ans.append(pre_xor[query[1]])
            else:
                ans.append(pre_xor[query[1]] ^ pre_xor[query[0] - 1])
        return ans