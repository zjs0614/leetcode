class Solution {
    public void rotate(int[] nums, int k) {
      /*
        Analysis:
          - nums size: s
          - if k % s == 0: return nums
          - reset k = k % s
          - inplace:
            - start from i, recycle j = j+k until j == i
            - if k and s have no common div, then only from 1
       */
      int s = nums.length;
      k = k % s;
      
      int count = this.gcd(k, s);

      for (int i=0; i<count; i++) {
        int start = i;
        int prev_val = nums[start];
        do {
          int next = (start + k) % s;
          int tmp = nums[next];
          nums[next] = prev_val;
          prev_val = tmp;
          start = next;
        } while (start != i);
      }
    }

    /**
      Return great common div of x and y
     */
    private int gcd(int x, int y) {
      return y > 0 ? gcd(y, x % y) : x;
    }
}



