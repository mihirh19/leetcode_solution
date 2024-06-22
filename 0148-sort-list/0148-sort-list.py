# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def findmid(head):
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def mergeTwo(left, right):
            dum = ListNode(-1)
            tmp = dum
            while left and right:
                if left.val < right.val:
                    tmp.next = left
                    tmp = left
                    left = left.next
                else:
                    tmp.next = right
                    tmp = right
                    right = right.next
            
            if left:
                tmp.next = left
            else:
                tmp.next= right

            return dum.next
              
        if head is None or head.next is None:
            return head
        
        mid  = findmid(head)
        right = mid.next
        mid.next = None
        left  = head

        left = self.sortList(left)
        right = self.sortList(right)
        return mergeTwo(left, right)




        