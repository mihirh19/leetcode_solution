import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for num in nums:
            if nums.count(num) > n//3:
                if num not in res:
                    res.append(num)
        
        return res

        
        