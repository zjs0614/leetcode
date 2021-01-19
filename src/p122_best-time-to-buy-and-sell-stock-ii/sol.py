class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None or len(prices) <= 1:
            return 0
        
        current = prices[0]
        result = 0
        for price in prices[1:]:
            if price > current:
                result = result + price - current
            current = price
        return result