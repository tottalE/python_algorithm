class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
            
        for i in range(0, len(prices)-1, 1):
            profit = max(prices[i+1:]) - prices[i]
            max_profit = max(max_profit, profit)

        return max_profit


            

        
