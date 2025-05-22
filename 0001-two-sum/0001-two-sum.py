class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
    Optimized Solution using Hash Map
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
        num_map = {}  # value -> index
    
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
    
        return []