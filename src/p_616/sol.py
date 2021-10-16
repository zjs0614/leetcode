class Solution:

  def getNewLast(self, s, words, i, cur_last):
    for word in words:
      l = len(word)
      if i + l > cur_last and s[i:i+l] == word:
          cur_last = i + l
    return cur_last

  def addBoldTag(self, s: str, words: List[str]) -> str:
    """
      Cases:
        1) 
    """

    if not words:
      return s

    bold_pos_arr = []

    for i, letter in enumerate(s):
      if bold_pos_arr and bold_pos_arr[-1][1] >= i:
        bold_pos_arr[-1][1] = self.getNewLast(s, words, i, bold_pos_arr[-1][1])
      else:
        cur_last = self.getNewLast(s, words, i, i)
        if cur_last > i:
          bold_pos_arr.append([i, cur_last])

    res, prev = "", 0

    for start, end in bold_pos_arr:
      res += s[prev:start] + "<b>" + s[start:end] + "</b>"
      prev = end

    if prev < len(s):
      res += s[prev:]
    
    return res