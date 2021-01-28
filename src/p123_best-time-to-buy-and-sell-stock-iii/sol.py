class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) <= 1:
            return 0
            
        profit = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = float('-inf'), float('-inf')
        profit[0][2][0], profit[0][2][1] = float('-inf'), float('-inf')

        for index, price in enumerate(prices[1:]):
            index = index + 1
            profit[index][0][0] = profit[index-1][0][0]
            profit[index][0][1] = max(profit[index-1][0][1], profit[index-1][0][0] - price)
            
            profit[index][1][0] = max(profit[index-1][1][0], profit[index-1][0][1] + price)
            profit[index][1][1] = max(profit[index-1][1][1], profit[index-1][1][0] - price)

            profit[index][2][0] = max(profit[index-1][2][0], profit[index-1][1][1] + price)
        
        return max(profit[index][0][0], profit[index][1][0], profit[index][2][0])
