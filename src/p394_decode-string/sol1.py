class Solution:
  def decodeString(self, s: str) -> str:
    """
    Args:
      - s: [1, 30], lower en, digits [1, 300], "[]" and valid
    Returns:
      - str: decoded string

    Analysis:
      - back tracking: 
        decode each pair into:
          - num
          - s_inside
          => s = n * s_inside
        pass s_inside into recursive call
    """
    res, i = self.decodeRecursive(s)
    return res
  
  def decodeRecursive(self, s):
    res = ""
    num, s_inside = "", ""
    i = 0
    while i < len(s):
      l = s[i]
      if self.is_digit(l):
        num += l
      elif self.is_lower_letter(l):
        res += l
      elif l == "[":
        s_inside, j = self.decodeRecursive(s[i+1:])
        res += int(num) * s_inside
        num, s_inside = "", ""
        i += j + 1
      elif l == "]":
        return res, i
      i += 1
    return res, i

    
  def is_lower_letter(self, l):
    return ord(l) >= ord("a") and ord(l) <= ord("z")
  def is_digit(self, l):
    return ord(l) >= ord("0") and ord(l) <= ord("9")

    