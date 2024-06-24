class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()[::-1]
        result=''
        for i in a:
            result= result + i+ ' '
        return result[:-1]