class Solution {
  public int evalRPN(String[] tokens) {
      Deque<Integer> nums = new LinkedList<Integer>();
      for (int i=0; i<tokens.length; i++) {
        String token = tokens[i];
        if (this.isOperator(token)) {
          int v2 = nums.pop();
          int v1 = nums.pop();
          nums.push(this.calculate(v1, v2, token));
        } else {
          nums.push(Integer.parseInt(token));
        }
      }
      return nums.pop();
  }

  private boolean isOperator(String token) {
      return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/");
  }

  private int calculate(int v1, int v2, String operator) {

      switch (operator) {
        case "+":
          return v1 + v2;
        case "-":
          return v1 - v2;
        case "*":
          return v1 * v2;
        case "/":
          return (int)(v1 / v2);
      }

      return -1;
  }
}