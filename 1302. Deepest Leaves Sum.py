# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        #### DFS check length ####
        # deepest = 0
        # ans = 0
        # deep = 0
        # path = [root.val]
        # stack = [(root, path)]
        # while stack:
        #     node = stack.pop()
        #     current = node[0]
        #     if current:
        #         path = node[1]
        #         deep += 1
        #         if current.left:
        #             stack.append((current.left, path + [current.left.val]))
        #         if current.right:
        #             stack.append((current.right, path + [current.right.val]))
        #         if not current.left and not current.right:
        #             if len(path) == deepest:
        #                 ans += path[-1]
        #             if len(path) > deepest:
        #                 deepest = len(path)
        #                 ans = path[-1]
        # return ans
        
        #### DFS check level ####
        # deepest = 0
        # ans = 0
        # level = 1
        # stack = [(root, level)]
        # while stack:
        #     node = stack.pop()
        #     current = node[0]
        #     if current:
        #         level = node[1]
        #         if current.left:
        #             stack.append((current.left, level + 1))
        #         if current.right:
        #             stack.append((current.right, level + 1))
        #         if not current.left and not current.right:
        #             if level == deepest:
        #                 ans += current.val
        #             if level > deepest:
        #                 deepest = level
        #                 ans = current.val
        # return ans
        
        #### BFS ####
        ans = 0
        level = 1
        num = []
        counter = 0
        que = deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node:
                counter += 1
                num.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                if counter == level:
                    level = len(que)
                    counter = 0
                    ans = sum(num)
                    num = []
        return ans