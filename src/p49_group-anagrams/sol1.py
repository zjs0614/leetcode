class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      """
      Args:
        - strs: List[str], length: [1, 10^4], str: en lowercase [0, 100]
      Returns:
        - List[List[str]]: group anagrams

      Analysis:
        - for each str, convert it to: n_letter combinations
        - build key for each anagram group
        - hash map for each anagram group
      
      Complexity:
        - Time: O(n * log(n))
        - Space: O(n)
      """
      mem = {}

      for s in strs:
        count_map = {}
        for letter in s:
          if letter not in count_map:
            count_map[letter] = 0
          count_map[letter] += 1
        key = ""
        for i in range(0, 26):
          l = chr(ord("a") + i)
          if l in count_map:
            key += str(count_map[l]) + "_" + l
        if key not in mem:
          mem[key] = []
        mem[key].append(s)
      
      return list(mem.values())









