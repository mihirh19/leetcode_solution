# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findNode(tmp, k):
            cnt =1
            while tmp:
                if cnt==k:
                    return tmp
                cnt+=1
                tmp = tmp.next
            return tmp

        if not head or k==0:
            return head
        
        tail = head
        le =1
        while tail.next:
            le+=1
            tail = tail.next
        
        if k%le ==0:
            return head
        k = k %le

        tail.next = head
        newLastNode=  findNode(head, le-k)

        head = newLastNode.next
        newLastNode.next = None

        return head
