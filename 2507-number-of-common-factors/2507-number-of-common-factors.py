class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n  = min(a,b)
        co = 0

        for i in range(1,n+1):
            if a%i==0 and b%i==0:
                co +=1
        
        return co
        