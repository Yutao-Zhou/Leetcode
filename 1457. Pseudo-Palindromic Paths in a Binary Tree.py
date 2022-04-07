# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        #### DFS frequency dic ####
        # ans = 0
        # path = {root.val: 1}
        # stack = [(root, path)]
        # while stack:
        #     node = stack.pop()
        #     path = node[1]
        #     if node[0].left:
        #         leftpath = path.copy()
        #         if node[0].left.val in leftpath:
        #             leftpath[node[0].left.val] += 1
        #         if node[0].left.val not in leftpath:
        #             leftpath[node[0].left.val] = 1
        #         stack.append((node[0].left, leftpath))
        #     if node[0].right:
        #         rightpath = path.copy()
        #         if node[0].right.val in rightpath:
        #             rightpath[node[0].right.val] += 1
        #         if node[0].right.val not in rightpath:
        #             rightpath[node[0].right.val] = 1
        #         stack.append((node[0].right, rightpath))
        #     if not node[0].left and not node[0].right:
        #         counter = 0
        #         for i in path.values():
        #             if i % 2 == 1:
        #                 counter += 1
        #         if counter <= 1:
        #             ans += 1
        # return ans
        
        #### BFS set ####
        ans = 0
        odd = set([root.val])
        que = deque([(root, odd)])
        while que:
            node = que.pop()
            odd = node[1]
            if node[0]:
                if node[0].left:
                    leftodd = odd.copy()
                    if node[0].left.val in leftodd:
                        leftodd.remove(node[0].left.val)
                    elif node[0].left.val not in leftodd:
                        leftodd.add(node[0].left.val)
                    que.append((node[0].left, leftodd))
                if node[0].right:
                    rightodd = odd.copy()
                    if node[0].right.val in rightodd:
                        rightodd.remove(node[0].right.val)
                    elif node[0].right.val not in rightodd:
                        rightodd.add(node[0].right.val)
                    que.append((node[0].right, rightodd))
                if not node[0].left and not node[0].right:
                    if len(node[1]) <= 1:
                        ans += 1
        return ans