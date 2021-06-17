class Solution {
  /**
    Analysis:
      -  gas = [3,4,5,1,2]
      - cost = [5,1,2,3,4]
                [-2,1,4,2,0]
      - sum_diff = [-2, -4, -6, -3, 0]
      - start at i
        - sum_diff[i] - sum_diff[i-1]
  */
  public int canCompleteCircuit(int[] gas, int[] cost) {
      if (gas.length == 0 || cost.length == 0) {
          return -1;
      }
      int lowest_sum_diff_pos = -1;
      int lowest_sum_diff = 0;
      int sum_diff = 0;
      for (int i=0; i<gas.length; i++) {
          sum_diff += gas[i] - cost[i];
          if (sum_diff < lowest_sum_diff) {
            lowest_sum_diff = sum_diff;
            lowest_sum_diff_pos = i;
          }
      }
      return sum_diff >= 0 ? (lowest_sum_diff_pos+1) % gas.length : -1;
  }
}