class Solution:
  def search(self, nums: List[int], target: int) -> int:
    """
    Args:
    Returns:
    Constraints:
    Analysis:
      - binary search problem with pivot
      - nums[i]..nums[j]..nums[k]: j=(i+k)/2
        - if nums[i] < nums[k]:
            in order
            -1 if target > nums[k] or target < nums[i]
            else binary_search
          else:
            if nums[i]<nums[j]:
              nums[i:j] in order
              nums[j:k] out of order
              if target > nums[j] or target < nums[k]:
                search(target, j,k)
              elif target > nums[i] and target < nums[j]:
                search(target, i,j)
              else:
                return -1
            else:
              nums[i:j] out of order
              nums[j:k] in order
              if target > nums[j] and target < nums[k]:
                search(target, j,k)
              elif target < nums[j] or target > nums[i]:
                search(target, i,j)
              else:
                return -1
    """
    if not nums:
      return -1
    if len(nums) == 1:
      return -1 if nums[0] != target else 0
    i, k = 0, len(nums)-1
    j = int((i+k)/2)

    if nums[i] == target:
      return i
    elif nums[j] == target:
      return j
    elif nums[k] == target:
      return k

    if nums[i] < nums[k]:
      if target < nums[i] or target > nums[k]:
        return -1
      else:
        if target == nums[j]:
          return j
        elif target < nums[j]:
          return self.search(nums[i:j+1], target)
        else:
          res = self.search(nums[j+1:k+1], target)
          return res if res < 0 else j + 1 + res
    else:
      if nums[i]<nums[j]:
        if target > nums[j] or target < nums[k]:
          res = self.search(nums[j+1:k+1], target)
          return res if res < 0 else j + 1 + res
        elif target > nums[i] and target < nums[j]:
          return self.search(nums[i:j+1], target)
        else:
          return -1
      else:
        if target > nums[j] and target < nums[k]:
          res = self.search(nums[j+1:k+1], target)
          return res if res < 0 else j + 1 + res
        elif target < nums[j] or target > nums[i]:
          return self.search(nums[i:j+1], target)
        else:
          return -1















