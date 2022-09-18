# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        #### Hash and Iteritive Construct ####
        treeValueMap = {}
        noParrent = set(node[0] for node in descriptions)
        for node in descriptions:
            noParrent.discard(node[1])
            if node[1] in treeValueMap:
                if node[0] not in treeValueMap:
                    parent = TreeNode(node[0])
                    treeValueMap[node[0]] = parent
            else:
                children = TreeNode(node[1])
                treeValueMap[node[1]] = children
                if node[0] not in treeValueMap:
                    parent = TreeNode(node[0])
                    treeValueMap[node[0]] = parent
            if node[2] == 0:
                treeValueMap[node[0]].right = treeValueMap[node[1]]
            if node[2] == 1:
                treeValueMap[node[0]].left = treeValueMap[node[1]]
        return treeValueMap[list(noParrent)[0]]