# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for l in lists:
            p = l
            while p:
                heappush(h,p.val)
                p = p.next
        
        head = ListNode(0)

        curr = head

        while len(h)!=0:
            curr.next = ListNode(heappop(h))
            curr = curr.next
        
        return head.next