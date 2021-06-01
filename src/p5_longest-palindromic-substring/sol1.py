class Solution:
  def longestPalindrome(self, s: str) -> str:
    """
    Args:
      s: str-[1, 1000], only digits and en lowercase and uppercase
    Returns:
      str: longest palindrome sub string.
    
    Analysis:
      1) search problem:
        - palindromic substring
        - longest (any)
      2) palindromic: middle expand
        - 1 middle: e.g. aba
        - 2 middles: e.g. abba
      3) special cases:
        - any s[i] counted as one palindromic substring
        - if s[i:j] is a palindromic substring: 0<=i<j<=len(s)
          - if k or (len(s) - k) <= (j-i-1) / 2, no need to check 1 middle case for k
          - if k or (len(s) - k) <= (j-i-2) / 2, no need to check 2 middle case for k
    Efficiency:
      Space: O(1): left, right, cur pointer, cur max, 
      Time:  O(n*n*2) => O(n^2)
    """
    if not s:
      return ""

    res, max_size, size = s[0], 1, len(s)

    for i, letter in enumerate(s):
      # 1 middle
      if i > (max_size-1) / 2 and (size - i - 1) > (max_size-1) / 2:
        left, right = i-1, i+1
        while left >= 0 and right < size and s[left] == s[right]:
          if right - left + 1 > max_size:
            max_size = right - left + 1
            res = s[left:right+1]
          left -= 1
          right += 1

      # 2 middles
      if i+1 < size and i > (max_size-2) / 2 and (size - i - 1) > (max_size-2) / 2 and s[i+1] == letter:
        left, right = i, i+1
        while left >= 0 and right < size and s[left] == s[right]:
          if right - left + 1 > max_size:
            max_size = right - left + 1
            res = s[left:right+1]
          left -= 1
          right += 1
    return res


