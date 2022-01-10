# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #### not real solution ####
        # check = []
        # while head:
        #     check.append(head.val)
        #     head = head.next
        # return check == check[::-1]
        
        #### stack ####
        # length, start = 0, 0
        # stack = []
        # h, l = head, head
        # while l:
        #     length += 1
        #     stack.append(l.val)
        #     l = l.next
        # if length % 2 == 0:
        #     length //= 2
        #     start = length
        # else:
        #     length //= 2
        #     start = length + 1
        # stack = stack[:length]
        # while h:
        #     if start != 0:
        #         start -= 1
        #     elif start == 0:
        #         if h.val == stack[-1]:
        #             stack.pop()
        #         else:
        #             return False
        #     h = h.next
        # return stack == []
        
        #### slow fast pointer, reverse second half####
        previous = None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        previous = slow
        slow = slow.next
        previous.next = None
        while slow:
            cache = slow.next
            slow.next = previous
            previous = slow
            slow = cache
        fast = head
        slow = previous
        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next
        return True