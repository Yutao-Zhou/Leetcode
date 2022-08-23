"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, adjList: 'Node') -> 'Node':
        #### Iteritive BFS ####
        # if not adjList:
        #     return None
        # ans, queue, visited = {}, deque([adjList]), set()
        # while queue:
        #     node = queue.popleft()
        #     if node not in visited:
        #         visited.add(node)
        #         if node not in ans:
        #             ans[node] = Node(node.val)
        #         for n in node.neighbors:
        #             if n not in ans:
        #                 ans[n] = Node(n.val)
        #             ans[node].neighbors.append(ans[n])
        #             queue.append(n)
        # return ans[adjList]
        
        #### Iteritive DFS ####
        # if not adjList:
        #     return None
        # ans, stack, visited = {}, [adjList], set()
        # while stack:
        #     node = stack.pop()
        #     if node not in visited:
        #         visited.add(node)
        #         if node not in ans:
        #             ans[node] = Node(node.val)
        #         for n in node.neighbors:
        #             if n not in ans:
        #                 ans[n] = Node(n.val)
        #             ans[node].neighbors.append(ans[n])
        #             stack.append(n)
        # return ans[adjList]
        
        #### Recursive DFS ####
        def DFSCopy(node):
            if node in visited:
                return
            visited.add(node)
            if node not in ans:
                ans[node] = Node(node.val)
            for n in node.neighbors:
                if n not in ans:
                    ans[n] = Node(n.val)
                ans[node].neighbors.append(ans[n])
                DFSCopy(n)
        if not adjList:
            return None
        ans, visited = {}, set()
        DFSCopy(adjList)
        return ans[adjList]