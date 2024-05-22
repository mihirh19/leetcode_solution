class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(e for e in s if e.isalnum())
        if len(s) < 1:
            return True
        return Solution.rec(0, s)
    
    @staticmethod
    def rec(i, s):
        if i >= len(s) // 2:
            return True
        if s[i] != s[len(s) - i - 1]:
            return False
        return Solution.rec(i + 1, s)