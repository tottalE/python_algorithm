class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_num = 100001
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_num:
                min_num = prices[i]
            elif prices[i] > min_num:
                max_profit = max(max_profit, prices[i] - min_num)

        return max_profit
