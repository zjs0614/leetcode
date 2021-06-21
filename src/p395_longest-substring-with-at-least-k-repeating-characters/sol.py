class Solution:
  def longestSubstring(self, s: str, k: int) -> int:
    """
    Analysis:
      - count map first, with number of invalid char: 
        - e.g. k=3 {"a":2, "b": 3}, num_invalid = 1
        - left=0, right=length-1, moving middle
          - stop when num_invalid == 0
          - if count_map[s[left]] < k:
              - move left to right
            elif count_map[s[right]] < k:
              - move right to left
          - else split string into different parts
    """
    count_map = {}
    invalid_char_set = set()
    for letter in s:
      if letter not in count_map:
        count_map[letter] = 0
      count_map[letter] += 1
      if count_map[letter] < k:
        invalid_char_set.add(letter)
      elif letter in invalid_char_set:
        invalid_char_set.remove(letter)

    if len(count_map) == len(invalid_char_set):
      return 0
    elif len(invalid_char_set) == 0:
      return len(s)
    else:
      points = [-1]
      for i, letter in enumerate(s):
        if letter in invalid_char_set:
          points.append(i)
      res = 0
      for i, point in enumerate(points):
        sub_res = self.longestSubstring(s[point+1:points[i+1]], k) if i < len(points)-1 \
            else self.longestSubstring(s[point+1:], k)
        if sub_res > res:
          res = sub_res
      return res





