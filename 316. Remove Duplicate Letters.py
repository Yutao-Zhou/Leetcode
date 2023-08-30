class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #  Monotonic stack
        occurance = {}
        seen = set()
        for i in range(len(s)):
            occurance[s[i]] = i
        stack = []
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] <= stack[-1] and i < occurance[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(s[i])
                seen.add(s[i])
        return "".join(stack)