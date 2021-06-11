class Solution:
  def myAtoi(self, s: str) -> int:
    sign, num = None, 0
    for i in s:
      if i >= "0" and i <= "9":
        if sign is None:
          sign = 1
        num = num * 10 + int(i)
      else:
        if sign is None:
          if i == "-":
            sign = -1
          elif i == "+":
            sign = 1
          elif i != " ":
            break
        else:
          break

    if sign is not None and sign > 0:
      return min(num, 2 ** 31 - 1)
    elif sign is not None and sign < 0: 
      return max(-num, - 2 ** 31)
    else:
      return 0