class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_value = prices[0]
        for value in prices[1:]:
            new_res = value - min_value
            result = result if new_res <= result else new_res
            min_value = min_value if min_value <= value else value
        return result