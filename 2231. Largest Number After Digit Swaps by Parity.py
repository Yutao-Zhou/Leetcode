class Solution:
    def largestInteger(self, num: int) -> int:
        #### Heap recreate answer ####
        import heapq
        even = []
        odd = []
        num = str(num)
        ans = [0] * len(num)
        if int(num[0]) % 2:
            odd_start = True
        for i in range(len(num)):
            if int(num[i]) % 2:
                heapq.heappush(odd, -int(num[i]))
                ans[i] = 1
            else:
                heapq.heappush(even, -int(num[i]))
        for i in range(len(ans)):
            if ans[i] % 2:
                ans[i] = str(-heapq.heappop(odd))
            else:
                ans[i] = str(-heapq.heappop(even))
        return int("".join(ans))