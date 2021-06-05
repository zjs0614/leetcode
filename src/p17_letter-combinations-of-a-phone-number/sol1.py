class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    """
    Args:
    Returns:
    Constraints:
    Analysis:
      - permutation problem
    """
    if not digits:
      return []
    letters = [
      "abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"
    ]
    digit_mapping = {}
    for i in range(2, 10):
      digit_mapping[str(i)] = [l for l in letters[i-2]]
    return self.getCombinations(digits, digit_mapping)
  
  def getCombinations(self, digits, mem):
    if digits in mem:
      return mem[digits]
    mid = int(len(digits)/2)
    left = self.getCombinations(digits[0:mid], mem)
    right = self.getCombinations(digits[mid:], mem)
    res = []

    for l in left:
      for r in right:
        res.append(l+r)
    mem[digits] = res
    return res




