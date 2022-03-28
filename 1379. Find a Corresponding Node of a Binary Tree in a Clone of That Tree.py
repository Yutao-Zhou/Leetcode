# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        #### BFS ####
        # que = deque()
        # que.append(cloned)
        # while que:
        #     node = que.popleft()
        #     if node:
        #         if node.val == target.val:
        #             return node
        #         if node.left:
        #             que.append(node.left)
        #         if node.right:
        #             que.append(node.right)
        
        #### DFS ####
        # stack = []
        # stack.append(cloned)
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         if node.val == target.val:
        #             return node
        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.right)
        
        #### Real solution with saved path ####
        ans = cloned
        stack = []
        path = []
        stack.append((original, path))
        while stack:
            node = stack.pop()
            current = node[0]
            if current:
                path = node[1]
                if current == target:
                    break
                if current.left:
                    stack.append((current.left, path + ["L"]))
                if current.right:
                    stack.append((current.right, path + ["R"]))
        for turn in path:
            if turn == "L":
                ans = ans.left
            if turn == "R":
                ans = ans.right
        return ans