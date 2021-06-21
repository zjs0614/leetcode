class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    """
    Analysis:
      - if there is a solution at index i:
        - sum(gas) >= sum(cost)
        - let sum_diff[p] = cost[p] - gas[p] + sum_diff[p-1]
          - argmin(sum_diff[x]): x = i-1
    """
    pre_sum_diff, min_diff, min_diff_index = 0, gas[0] - cost[0], 0

    for i in range(len(gas)):
      pre_sum_diff += gas[i] - cost[i]
      if pre_sum_diff < min_diff:
        min_diff = pre_sum_diff
        min_diff_index = i
    
    return -1 if pre_sum_diff < 0 else (min_diff_index + 1) % len(gas)


