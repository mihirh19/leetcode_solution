# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = ListNode(0)
        slow_ptr = prev
        prev.next= head
        fast_ptr = head

        if head:
            while(fast_ptr  and fast_ptr.next):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            
            slow_ptr.next = slow_ptr.next.next
            return prev.next