class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If all transactions are negative choose 0 max(0, all_transactions)
        # 1 Pass keeping track of the minimum value that we have so far to buy at. Calculate price of buying at minmum value and selling at current value. Keep updating minimum value and max profit

        # Edge cases: if there's 0 days: 0
        # If there's one day --> Also 0
        # If two days, if it is profitable buy-sell otherwise don't do anything
        if len(prices) <= 1: return 0

        best, min_value = 0, prices[0]
        for price in prices:
            best = max(price-min_value, best)
            min_value = min(min_value, price)

        return best