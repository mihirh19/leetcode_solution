class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            carry = sum // 10
            head.next = ListNode(sum % 10)
            head = head.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
    
        return dummy.next