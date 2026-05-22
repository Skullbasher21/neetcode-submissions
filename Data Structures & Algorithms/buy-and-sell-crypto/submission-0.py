class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        if prices == []:
            return 0
        lower = prices[0]
        for p in range(len(prices) - 1):
            if prices[p + 1] < lower:
                lower = prices[p + 1]
            dp[p] = prices[p + 1] - lower
        return max(dp)
            
            