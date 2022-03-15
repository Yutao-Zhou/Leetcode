class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #### BFS: creat graph, find all connection, and find max length ####
        connect = []
        ans = []
        maxLen = 0
        
        for a in range(len(bombs)):
            cache = []
            for b in range(len(bombs)):
                if ((bombs[b][0] - bombs[a][0]) ** 2 + (bombs[b][1] - bombs[a][1]) ** 2) ** 0.5 <= bombs[a][2] and a != b:
                    cache.append(b)
            connect.append(cache)
        for i in range(len(bombs)):
            que = [i]
            path = []
            seen = set()
            while que != []:
                current = que.pop(0)
                if current not in seen:
                    seen.add(current)
                if path == []:
                    path.append(current)
                for i in connect[current]:
                    if i not in seen:
                        path.append(i)
                        que.append(i)
                        seen.add(i)
            ans.append(path)
        
        for i in ans:
            if len(i) > maxLen:
                maxLen = len(i)
        return maxLen