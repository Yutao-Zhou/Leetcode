class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        #### BFS ####
        queue = deque()
        queue.append((0, False))
        seen = set()
        for f in forbidden:
            seen.add((f, True))
            seen.add((f, False))
        furthest = max(x, max(forbidden)) + a + b
        level = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                current = queue.popleft()
                if current[0] == x:
                    return level
                if current[0] + a <= furthest and (current[0] + a, False) not in seen:
                    queue.append((current[0] + a, False))
                    seen.add((current[0] + a, False))
                if not current[1]:
                    if 0 <= current[0] - b and (current[0] - b, True) not in seen:
                        queue.append((current[0] - b, True))
                        seen.add((current[0] - b, True))
            level += 1
        return -1