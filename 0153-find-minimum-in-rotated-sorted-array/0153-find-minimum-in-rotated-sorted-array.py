class Solution:
    def findMin(self, nums: List[int]) -> int:
        l ,h = 0, len(nums)-1
        ans = float('inf')
        while l <= h:
            mid = int((l+h)/2)
            if nums[l] <= nums[mid]:
                ans = min(ans, nums[l])
                l =mid+1
            else:
                ans = min(ans, nums[mid])
                h = mid-1
        return ans

        