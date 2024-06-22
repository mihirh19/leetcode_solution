class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        val = []
        temp = head
        while temp:
            val.append(temp.val)
            temp = temp.next

        return val == val[::-1]
