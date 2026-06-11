class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        x = 0
        y = 1
        while y < len(prices):
            diff = prices[y] - prices[x]
            m = max(m, diff)
            if diff < 0:
                x = y
            y += 1

        return m
            