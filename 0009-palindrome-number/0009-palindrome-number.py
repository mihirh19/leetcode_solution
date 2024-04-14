class Solution:

    def isPalindrome(self, x: int) -> bool:
        temp = x
        new_num = 0
        while temp > 0:
            new_num = new_num * 10 + temp % 10
            temp //= 10

        return x == new_num