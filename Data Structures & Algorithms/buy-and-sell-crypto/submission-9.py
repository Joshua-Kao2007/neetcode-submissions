class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L,R = 0,0
        best_profit = -1
        while R < len(prices):
            if prices[R] > prices[L]:
                best_profit = max(best_profit, prices[R]-prices[L])
            else:
                L = R
            R += 1
        return max(best_profit, 0)