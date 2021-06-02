class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    """
    Args:
      - coins: list of integers: available coins [1, 2^31-1], length[1,12]
      - amount [0, 10^4]
    Returns:
      - minimum number of coins needed
    
    Analysis:
      - result = min(coins, amount-coins[i]) for each available coins[i]
      - if amount % coins[i] == 0 and coins[i] is the max, return amount / coins[i]
    """
    mem = {}
    for coin in coins:
      mem[coin] = 1
    return self.coinChangeCount(sorted(coins, reverse=True), amount, 0, mem)
  
  def coinChangeCount(self, coins, amount, count, mem):
    if amount <= 0:
      return count
    elif amount < coins[-1]:
      return -1
    elif amount in mem:
      return -1 if mem[amount] == -1 else count + mem[amount]
    elif amount % coins[0] == 0:
      mem[amount] = int(amount / coins[0])
      return count + mem[amount]
    
    res = -1
    for coin in coins:
      if coin == amount:
        res = count + 1
        break
      elif coin < amount:
        new_res = self.coinChangeCount(coins, amount-coin, count + 1, mem)
        if new_res > 0 and (new_res < res or res == -1):
          res = new_res
    mem[amount] = -1 if res == -1 else res - count
    return res