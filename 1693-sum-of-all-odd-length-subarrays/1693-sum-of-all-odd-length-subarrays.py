class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n  = len(arr)
        to = []
        for i in range(n):
            cus = 0
            for j in range(i, n):
                cus+=arr[j]
                if (j-i+1)%2 !=0:
                    to.append(cus)
        
        return sum(to)
