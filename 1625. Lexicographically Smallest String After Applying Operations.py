class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        #### BFS Brute force ####
        # ans = s
        # seen = set()
        # queue = deque()
        # queue.append(s)
        # while queue:
        #     current = queue.popleft()
        #     if current not in seen:
        #         queue.append(current[-b:] + current[:-b])
        #         currentList = list(current)
        #         for i in range(1, len(currentList), 2):
        #             currentList[i] = str((int(currentList[i]) + a) % 10)
        #         queue.append("".join(currentList))
        #     for i in range(len(current)):
        #         if current[i] > ans[i]:
        #             break
        #         elif current[i] < ans[i]:
        #             ans = current 
        #     seen.add(current)
        # return ans

        #### DFS Brute force ####
        ans = s
        seen = set()
        queue = deque()
        queue.append(s)
        while queue:
            current = queue.pop()
            if current not in seen:
                queue.append(current[-b:] + current[:-b])
                currentList = list(current)
                for i in range(1, len(currentList), 2):
                    currentList[i] = str((int(currentList[i]) + a) % 10)
                queue.append("".join(currentList))
            for i in range(len(current)):
                if current[i] > ans[i]:
                    break
                elif current[i] < ans[i]:
                    ans = current 
            seen.add(current)
        return ans