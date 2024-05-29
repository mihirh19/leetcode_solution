class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ma= {}
        for i in range(len(nums)):
            a = nums[i]
            more = target - a
            if more in ma:
                return [i,ma[more]]

            if a not in ma:
                ma[a] = i