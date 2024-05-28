class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        has = {}

        for i in range(n):
            has[nums[i]]=True
        
        for i in range(n+1):
            if i  not in has:
                return i
        return -1
        