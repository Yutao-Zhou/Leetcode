class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #### DFS find all rout and count number of routs ####
#         connection = []
#         cache = []
        
#         seen = set()
#         stack = []
#         path = []
#         ans = []
        
#         for i in isConnected:
#             for j in range(len(i)):
#                 if i[j] == 1:
#                     cache.append(j)
#             connection.append(cache)
#             cache = []
#         for i in range(len(connection)):
#             if i in connection[i]:
#                 connection[i].remove(i)
#         for i in range(len(connection)):
#             if connection[i] == []:
#                 ans.append([i])
#                 seen.add(i)
#         while len(seen) != len(isConnected):
#             remain = set(range(len(isConnected))).difference(seen)
#             stack.append(list(remain)[0])
#             while stack != []:
#                 current = stack.pop()
#                 if current not in seen:
#                     seen.add(current)
#                 if path == []:
#                     path.append(current)
#                 for i in connection[current]:
#                     if i not in seen:
#                         path.append(i)
#                         stack.append(i)
#                         seen.add(i)
#             ans.append(path)
#             path = []
#         return len(ans)
        
        #### BFS find all rout and count number of routs ####
        connection = []
        cache = []
        
        seen = set()
        que = []
        path = []
        ans = []
        
        for i in isConnected:
            for j in range(len(i)):
                if i[j] == 1:
                    cache.append(j)
            connection.append(cache)
            cache = []
        for i in range(len(connection)):
            if i in connection[i]:
                connection[i].remove(i)
        for i in range(len(connection)):
            if connection[i] == []:
                ans.append([i])
                seen.add(i)
        while len(seen) != len(isConnected):
            remain = set(range(len(isConnected))).difference(seen)
            que.append(list(remain)[0])
            while que != []:
                current = que.pop(0)
                if current not in seen:
                    seen.add(current)
                if path == []:
                    path.append(current)
                for i in connection[current]:
                    if i not in seen:
                        path.append(i)
                        que.append(i)
                        seen.add(i)
            ans.append(path)
            path = []
        return len(ans)