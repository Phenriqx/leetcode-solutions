from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i, j = 0, 1

        while j < len(prices):
            if prices[i] >= prices[j]:
                i = j

            elif prices[j] > prices[i]:
                curr_profit = prices[j] - prices[i]
                max_profit = max(max_profit, curr_profit)

            j += 1

        return max_profit