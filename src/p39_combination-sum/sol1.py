class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    """
    Args:
    Returns:
    Constraints:
    Analysis:
      - enumeration, unlimited times -> if target % number == 0 return [number] * int(target / number)
      - only positive integers -> no need to check after sum > target
      - unique sequence -> sorted first
    """
    return self.getCombinationSum(sorted(candidates), target)


  
  def getCombinationSum(self, sortedCandidates, target):
    if not sortedCandidates or target < sortedCandidates[0]:
      return []
    
    res = []
    for i, candidate in enumerate(sortedCandidates):
      if candidate > target:
        break
      elif candidate == target:
        res.append([candidate])
      else:
        next_res = self.getCombinationSum(sortedCandidates[i:], target-candidate)
        for c in next_res:
          res.append([candidate] + c)
    return res

