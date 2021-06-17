class Solution {
  public int numDecodings(String s) {
      return this.numDecodings(s, 0, new HashMap<Integer, Integer>());
  }

  public int numDecodings(String origin_s, int from, Map<Integer, Integer> mem) {
      if (mem.get(from) != null) {
          return mem.get(from);
      }
      String s = origin_s.substring(from);
      int size = s.length();
      if (size == 0) {
          return 0;
      } else if (size == 1) {
          return this.isValid(s) ? 1 : 0;
      }

      if (s.charAt(0) == '0') {
        return 0;
      }

      int res = 0;
      if (this.isValid(s.substring(0, 2))) {
        if (s.length() > 2) {
          int next = this.numDecodings(origin_s, from+2, mem);
          if (next > 0) {
            res += next;
          }
        } else{
          res += 1;
        }
      }
      if (this.isValid(s.substring(0, 1))) {
        int next = this.numDecodings(origin_s, from+1, mem);
        if (next > 0) {
          res += next;
        }
      }

      mem.put(from, res);
      return res;

  }

  private boolean isValid(String s) {
      int value = Integer.parseInt(s);
      return value >= 1 && value <= 26;
  }
}