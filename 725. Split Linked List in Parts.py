# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        start = head
        ans = []
        while head:
            head = head.next
            length += 1
        remainder = length % k
        for i in range(k):
            segment_start = start
            segment_len = length // k
            if remainder:
                segment_len += 1
                remainder -= 1
            for i in range(max(0, segment_len - 1)):
                if start:
                    start = start.next
            if start:
                tmp = start.next
                start.next = None
                start = tmp
            ans.append(segment_start)
        return ans