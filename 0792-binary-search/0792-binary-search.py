# Time: O(logn)
class Solution:
	def search(self, nums: List[int], target: int) -> int:
		def bSearch(nums, low, high, targ):
			if high >= low:
				mid = low+(high-low)//2
				if nums[mid] == targ:
					return mid
				elif nums[mid] > targ:
					return bSearch(nums, low, mid-1, targ)
				else:
					return bSearch(nums, mid+1, high, targ)
			else:
				return -1
		return bSearch(nums, 0, len(nums)-1, target)