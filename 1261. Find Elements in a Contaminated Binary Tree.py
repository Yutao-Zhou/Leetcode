# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#### Recover ####
# class FindElements:
#     def __init__(self, root: Optional[TreeNode]):
#         self.inTree = set()
#         def build(root, nums):
#             self.inTree.add(nums)
#             if root.left:
#                 build(root.left, nums * 2 + 1)
#             if root.right:
#                 build(root.right, nums * 2 + 2)
#         build(root, 0)

#     def find(self, target: int) -> bool:
#         return target in self.inTree

#### Tranverse and search ####
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
    def find(self, target: int) -> bool:
        if target == 0:
            return True
        binary = bin(target+1)[3:]                  # remove the useless first `1`
        l = len(binary)
        index = 0
        root = self.root 
        # use a new pointer `root` to traverse the tree
        currentNum = 0
        while index < l: # traverse the binary number from left to right
            if  binary[index] == '0':  # if it's 0, we have to go left
                root = root.left
                currentNum = currentNum * 2 + 1
            else:  # if it's 1, we have to go right
                root = root.right
                currentNum = currentNum * 2 + 2
            index += 1
            if not root:
                return False
            if currentNum == target:
                return True


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)