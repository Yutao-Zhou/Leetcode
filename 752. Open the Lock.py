class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #### BFS ####
        # seen = set()
        # queue = deque()
        # queue.append(("0000", 0))
        # while queue:
        #     current = queue.popleft()
        #     if current[0] == target:
        #         return current[1]
        #     if current[0] not in deadends and current[0] not in seen:
        #         seen.add(current[0])
        #         for i in range(4):
        #             queue.append((current[0][:i] + chr((ord(current[0][i]) - 47) % 10 + 48) + current[0][i + 1:], current[1] + 1))
        #             queue.append((current[0][:i] + chr((ord(current[0][i]) - 49) % 10 + 48) + current[0][i + 1:], current[1] + 1))
        # return -1
        
        #### Clearner BFS ####
        seen = set(deadends)
        queue = deque()
        queue.append(("0000", 0))
        while queue:
            current = queue.popleft()
            if current[0] == target:
                return current[1]
            if current[0] not in seen:
                seen.add(current[0])
                for i in range(4):
                    queue.append((current[0][:i] + chr((ord(current[0][i]) - 47) % 10 + 48) + current[0][i + 1:], current[1] + 1))
                    queue.append((current[0][:i] + chr((ord(current[0][i]) - 49) % 10 + 48) + current[0][i + 1:], current[1] + 1))
        return -1