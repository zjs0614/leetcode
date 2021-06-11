class Solution:
  def calculate(self, s: str) -> int:
    stack = [0]
    cur_num, sign = 0, "+"
    for i in s + "+":
      if i >= "0" and i <= "9":
        cur_num = cur_num * 10 + int(i)
      elif i == "+" or i == "-" or ((i == "*" or i == "/") and (sign == "*" or sign == "/")):
        stack.append(self.calculate2nums(stack.pop(), cur_num, sign))
        sign = i
        cur_num = 0
      elif (i == "*" or i == "/") and (sign == "+" or sign == "-"):
        stack.append(cur_num if sign == "+" else -cur_num)
        sign = i
        cur_num = 0
    return sum(stack)

  def calculate2nums(self, n1, n2, sign):
    if sign == "+":
      return n1 + n2
    elif sign == "-":
      return n1 - n2
    elif sign == "*":
      return n1 * n2
    elif sign == "/":
      return int(n1 / n2)