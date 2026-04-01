class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit_so_far = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit_so_far = max(max_profit_so_far, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_profit_so_far