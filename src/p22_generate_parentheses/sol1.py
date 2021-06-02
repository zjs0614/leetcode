class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    """
    Args:
      - n: [1, 8], number of parenntheses pairs
    Returns:
      - List[str]: list of valid combinations
    
    Analysis:
      - enumerate permutations
      - validation: () (()), not ())(
        => rules: any piece of time: num("(") >= num(")")
      - sol: using tree structure
        - (()()) -> one root with 2 children
      - sol: using stack
      - sol: using recursive back tracking
    """
    return self.back_tracking(n, 0, 0, [""])
  
  def back_tracking(self, n, num_open, num_close, res):
    new_res = []
    if num_open < n:
      new_res.extend(
        self.back_tracking(n, num_open+1, num_close, 
                    [line + "(" for line in res]))
    if num_close < n and num_close < num_open:
      new_res.extend(
        self.back_tracking(n, num_open, num_close+1, 
                  [line + ")" for line in res]))
    
    if num_open == n and num_close == n:
      new_res = res
    
    return new_res