class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Is current day the day that you buy or not?
        best = -1
        best_prev = float('inf')
        for price in prices:
            best = max(best, price-best_prev)
            best_prev = min(best_prev, price)
        return max(best,0)