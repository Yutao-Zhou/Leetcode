# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        #### Brute Force BFS and Two Space Priority Queue ####
        # priorityQue, que = deque([root.val]), deque([root])
        # while que:
        #     node = que.pop()
        #     if node:
        #         que.append(node.left)
        #         que.append(node.right)
        #         if len(priorityQue) < 2:
        #             if node.val < priorityQue[0]:
        #                 priorityQue.appendleft(node.val)
        #             if node.val > priorityQue[0]:
        #                 priorityQue.append(node.val)
        #         else:
        #             if node.val < priorityQue[0]:
        #                 priorityQue.appendleft(node.val)
        #                 priorityQue.pop()
        #             elif node.val > priorityQue[0] and node.val < priorityQue[1]:
        #                 priorityQue.pop()
        #                 priorityQue.append(node.val)
        # if len(priorityQue) == 1:
        #     return -1
        # return priorityQue[-1]
        
        #### Find Different Node ####
#         def checkChild(node):
#             if node:
#                 if node.val != root.val:
#                     differentNode.append(node.val)
#                     return
#                 checkChild(node.left)
#                 checkChild(node.right)
                
#         differentNode = []
#         checkChild(root)
#         if not differentNode:
#             return -1
#         return min(differentNode)
        #### Find Second Min Node ####
        v, ans, queue = root.val, float('inf'), deque([root])
        while queue:
            node = queue.popleft()
            if node:
                if node.val == v:
                    queue.append(node.left)
                    queue.append(node.right)
                elif node.val < ans:
                        ans = node.val
        if ans == float('inf'):
            return -1
        return ans