# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #### count length, reverse twice ####
        # previous = None
        # counter = 0
        # while head:
        #     current = head
        #     head = head.next
        #     current.next = previous
        #     previous = current
        #     counter += 1
        # counter = (counter + 1) // 2
        # head = previous
        # previous = None
        # while counter > 0:
        #     current = head
        #     head = head.next
        #     current.next = previous
        #     previous = current
        #     counter -= 1
        # return previous
        
        #### two pointer slow and fast ####
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow