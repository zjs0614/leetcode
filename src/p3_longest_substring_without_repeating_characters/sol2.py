class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    """
    Args:
      - s: string, [0, 5 * 10^4], digits, en, symbols, spaces
    Returns:
      - int: length of longest substring (non repeated char)

    Analysis:
      - searching problem
        - non-repeated sub string
        - max length
      - left, right pointers
        - dict: (char, index)
          - if s[i] not in dict:
              add s[i] to dict
              move right to i+1
          - elif s[i] in dict:
              dict[s[i]] -> left_new
              while left <= left_new:
                dict.pop(dict[s[left]])
                left += 1
          - keep update max res by comparing max length with current right - left + 1
      - special cases
        1) cur_max >= len(s) - left: then break
        2) s = "" -> 0
    """  
    if len(s) <= 1:
      return len(s)
    
    left, right, mem = 0, 0, {}
    size = len(s)
    res = 1

    while right < size and size - left > res:
      if s[right] not in mem:
        mem[s[right]] = right
        right += 1
        res = max(res, right - left)
      else:
        left_new = mem[s[right]]
        while left <= left_new:
          mem.pop(s[left])
          left += 1
          
    return res





