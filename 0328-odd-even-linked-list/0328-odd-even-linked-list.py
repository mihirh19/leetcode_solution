# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_p = ListNode()
        odd = odd_p
        even_p  = ListNode()
        even = even_p
        tmp = head
        idx = 1
        while tmp:
            if idx%2==0:
                even.next = tmp
                even = even.next
            else:
                odd.next = tmp
                odd = odd.next
            tmp = tmp.next
            idx+=1
        even.next = None
        odd.next = even_p.next
        return odd_p.next
        