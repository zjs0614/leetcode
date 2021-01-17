class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    records = {}
    for index, num in enumerate(nums):
        if target - num in records:
            return [index, records[target - num]]
        else:
            records[num] = index
    return []