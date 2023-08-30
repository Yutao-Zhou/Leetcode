class Solution:
    def smallestSubsequence(self, s: str) -> str:
        #  Monotonic stack
        occurance = {}
        seen = set()
        stack = []
        for i in range(len(s)):
            occurance[s[i]] = i
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i] <= stack[-1] and occurance[stack[-1]] > i:
                    seen.remove(stack.pop())
                stack.append(s[i])
                seen.add(s[i])
        return "".join(stack) 