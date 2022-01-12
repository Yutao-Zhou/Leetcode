class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        code += code
        if k < 0:
            for i in range(len(code) // 2, len(code)):
                ans.append(sum(code[i + k:i]))
        if k == 0:
            ans = [0] * (len(code) // 2)
        if k > 0:
            for i in range(0, len(code) // 2):
                ans.append(sum(code[i + 1:i + k + 1]))
        return ans