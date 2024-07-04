# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        su =0
        ans =[]
        tmp = tmp.next
        while tmp:
            if tmp.val!=0:
                su+=tmp.val
            else:
                ans.append(su)
                su=0
            tmp =tmp.next
        
        new_head = ListNode(0)
        tmp = new_head
        for n in ans:
            tmp.next = ListNode(n)
            tmp = tmp.next
        return new_head.next


            

        