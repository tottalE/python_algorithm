class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        min_num = 100001

        for i in range(len(prices)):
            if prices[i] < min_num:
                min_num = prices[i]
            elif prices[i] > min_num:
                profits.append(prices[i] - min_num)


        return max(profits)
