class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        presum=0
        dic = {}
        dic[0] =1
        for i in range(len(nums)):
            presum+=nums[i]
            if presum-k in dic:
                cnt+= dic[presum-k]
            dic[presum] = dic.get(presum,0)+1
        return cnt