class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #### Greedy Monotonic Stack ####
        stack = deque()
        for i in range(len(num)):
            while stack and num[i] < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k > 0:
            stack.pop()
            k -= 1
        while stack and stack[0] == "0":
            stack.popleft()
        if not stack:
            stack.append("0")
        return "".join(stack)