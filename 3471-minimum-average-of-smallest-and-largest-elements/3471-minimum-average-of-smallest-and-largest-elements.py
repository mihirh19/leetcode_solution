class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)//2
        arr =[]
        for i in range(n):
            x = max(nums)
            y = min(nums)
            avg = (x+y)/2
            arr.append(avg)
            nums.remove(x)
            nums.remove(y)
        
        return min(arr)