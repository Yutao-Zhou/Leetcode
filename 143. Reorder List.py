# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #### get second half, inverse and merge ####
        
#         # get second half of the linked list
#         slow, fast = head, head
#         while fast and fast.next:
#             fast = fast.next.next
#             if fast:
#                 slow = slow.next
#         secondHalf = slow.next
#         slow.next = None
        
#         # reverse second half
#         prev, curr = None, secondHalf
#         while curr:
#             n = curr.next
#             curr.next = prev
#             prev = curr
#             curr = n
            
#         # combine original with reversed second half
#         while prev:
#             n = head.next
#             head.next = prev
#             head = head.next
#             prev = head.next
#             head.next = n
#             head = head.next
        #### Brute Force ####
        
        # get number
        dummy, data = head, deque()
        while head:
            data.append(head.val)
            head = head.next
        head = dummy
        
        # revalue original list
        even = True
        while data:
            if even:
                head.val = data.popleft()
                even = False
            elif not even:
                head.val = data.pop()
                even = True
            head = head.next