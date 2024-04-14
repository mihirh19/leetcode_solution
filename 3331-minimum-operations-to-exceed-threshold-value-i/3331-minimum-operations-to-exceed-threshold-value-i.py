class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        su= 0
        for i in nums:
            if i < k:
                su +=1
        
        return su