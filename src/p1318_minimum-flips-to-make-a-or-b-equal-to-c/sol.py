class Solution:
  def minFlips(self, a: int, b: int, c: int) -> int:
    res = 0
    while a != 0 or b != 0 or c != 0:
      a1, b1, c1 = a & 1, b & 1, c & 1
      a >>= 1
      b >>= 1
      c >>= 1
      if c1 == 1 and a1 | b1 == 0:
        res += 1
      elif c1 == 0:
        if a1 == 1:
          res += 1
        if b1 == 1:
          res += 1
    return res
      