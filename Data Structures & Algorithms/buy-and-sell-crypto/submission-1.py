class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            if (prices[i] - prices[buy]) > profit and buy != i:
                profit = prices[i] - prices[buy]
            
        return profit
#prices=[5,1,5,6,7,1,10]
        