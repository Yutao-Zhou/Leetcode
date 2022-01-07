# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #### get length ####
#     def __init__(self, head: Optional[ListNode]):
#         self.head = head
#         node = head
#         self.numNodes = 0
#         while node:
#             self.numNodes += 1
#             node = node.next

#     def getRandom(self) -> int:
#             num = random.randint(0,self.numNodes - 1)
#             node = self.head
#             while num:
#                 node = node.next
#                 num -= 1
#             return node.val
    
    #### get value ####
#     def __init__(self, head: Optional[ListNode]):
#         self.head = head
#         node = head
#         self.num = []
#         while node:
#             self.num.append(node.val)
#             node = node.next

#     def getRandom(self) -> int:
#         i = random.randint(0,len(self.num) - 1)
#         return self.num[i]
    
    #### Reservoir Sampling ####
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        head = self.head
        ans = 0
        scope = 1
        while head:
            if random.random() < 1 / scope:
                ans = head.val
            head = head.next
            scope += 1
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()