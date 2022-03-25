class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        #### DFS ####
        stack = []
        stack.append(start)
        while stack:
            current = stack.pop()
            if arr[current] == 0:
                return True
            if current + arr[current] < len(arr):
                stack.append(current + arr[current])
            if current - arr[current] >= 0:
                stack.append(current - arr[current])
            arr[current] = float("inf")
        return False