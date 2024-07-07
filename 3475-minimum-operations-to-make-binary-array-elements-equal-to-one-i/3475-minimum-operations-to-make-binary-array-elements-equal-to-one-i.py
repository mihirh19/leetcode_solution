class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        co = 0

        for i in range(n-2):
            if nums[i]==0:
                nums[i]= nums[i]^1
                nums[i+1]=nums[i+1]^1
                nums[i+2] = nums[i+2]^1
                co+=1
        
        if all(x==1 for x in nums):
            return co
        return -1
