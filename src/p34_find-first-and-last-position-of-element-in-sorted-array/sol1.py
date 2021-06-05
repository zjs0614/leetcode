class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    """
    Analysis:
      - binary search with duplicate number, find start and end
    """
    if not nums:
      return [-1, -1]
    
    if target < nums[0] or target > nums[-1]:
      return [-1, -1]
    
    if len(nums) == 1:
      return [0, 0]
    
    mid = int((len(nums) - 1)/2)
    if nums[mid] < target:
      res = self.searchRange(nums[mid+1:], target)
      if res[0] >= 0:
        return [res[0] + mid + 1, res[1] + mid + 1]
      else:
        return res
    elif nums[mid] > target:
      res = self.searchRange(nums[0:mid], target)
      return res
    else:
      left_range = self.searchRange(nums[0:mid], target)
      right_range = self.searchRange(nums[mid+1:], target)
      return [min(mid, left_range[0] if left_range[0] >= 0 else mid),
                max(mid, right_range[1] + mid+1 if right_range[1] >= 0 else mid)]