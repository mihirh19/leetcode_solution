class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = len(nums) // 2
        set_n = set(nums)
        for ele in set_n:
            if nums.count(ele) > x:
                return ele
        