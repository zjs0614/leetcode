class Solution:
  def countAndSay(self, n: int) -> str:
    """
    Analysis:
      - 1: 1
      - 2: say "1" -> 11
      - 3: say "11" -> 21
      - 4: say "21" -> 1211
      - 5: say "1211" -> 111221
      - 6: say "111221" -> 312211
      - 7: say "312211" -> 13112221
      - 8: say "13112221" -> 1113213211
    """
    old = "1"
    for i in range(n-1):
      new, cur, count = "", "", 0
      for num in old:
        if num != cur:
          if count > 0:
            new += str(count) + cur
          cur = num
          count = 1
        else:
          count += 1
      if count > 0:
        new += str(count) + cur
      old = new
    return old