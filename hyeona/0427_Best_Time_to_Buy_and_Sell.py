class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = 10001
        max_profit = 0

        for price in prices:
            min_value = min(price,min_value)
            max_profit = max(price-min_value,max_profit)

        return max_profit
