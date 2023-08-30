class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        #### Sort and monotonic stack ####
        ans = 0
        stack = []
        properties.sort(key=lambda x:(x[0], -x[1]))
        for caracter in properties:
            while stack and caracter[1] > stack[-1][1] and caracter[0] > stack[-1][0]:
                stack.pop()
                ans += 1
            stack.append(caracter)
        return ans