class Solution:
    def countDigits(self, num: int) -> int:
        li  = list(str(num))
        res = 0
        for l in li:
            sd = int(l)
            if num % sd ==0:
                res+=1
        
        return res
                