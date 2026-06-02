class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        best = 0
        for i in range(len(prices)):
            best = max(best, prices[i] - m)
            if prices[i] < m:
                m = prices[i]

        return best