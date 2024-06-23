class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n  = len(nums)
        subs = 1 << n
        ans = []

        for num in range(subs):
            li = []
            for i in range(n):
                if num &(1<<i):
                    li.append(nums[i])
            ans.append(li)
        
        return ans

        
        