class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ma = 0
        alt = 0
        for i in range(len(gain)):
            alt += gain[i]
            ma = max(ma, alt)
        
        return ma

        