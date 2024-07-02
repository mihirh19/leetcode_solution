class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n)
        def rec(ind,nums, dp):
            if ind==0:
                return nums[ind]
            if ind < 0:
                return 0
            
            if dp[ind] !=-1:
                return dp[ind]
            p = nums[ind] + rec(ind-2, nums, dp)
            np = 0  + rec(ind-1, nums,dp)
            dp[ind] = max(p,np)
            return dp[ind]
        return rec(n-1,nums,dp)