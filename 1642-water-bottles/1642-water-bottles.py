class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ne=res=0

        while numBottles:
            res+=numBottles
            ne+=numBottles
            numBottles = ne//numExchange
            ne  = ne%numExchange
        return res