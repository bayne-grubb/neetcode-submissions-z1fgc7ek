class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit_so_far = 0

        for price in prices[1:]:
            if price < min_so_far:
                min_so_far = price
            max_profit_so_far = max(price - min_so_far, max_profit_so_far)
        return max_profit_so_far