class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit =0
        for i  in range(len(prices)):
            c = prices[i] - mini
            profit = max(profit,c)
            mini = min(mini, prices[i])
        
        return profit
