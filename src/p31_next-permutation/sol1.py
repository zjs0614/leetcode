class Solution:
  def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    """
    Args:
      - nums: List[int], [1, 100], number:[0, 100]
    Retuns:
      - inplace change to next permute

    Analysis:
      - e.g
        1,2,3 -> 1,3,2
        1,2,4,3 -> 1,3,2,4
        1,3,4,2 -> 1,4,2,3
        1,5,8,7,6,4 -> 1,6,4,5,7,8
        1,5,8,4,6,7 -> 
      - loop backwards
        if n[i] > n[i-1]
          a = i-1
          loop from i to end, find first item n[j] < n[a] -> b = j-1, c=j
          res = nums[0:i-1]
          res.append(b)
          res.reversely_append(nums[c:])
          res.append(a)
          res.reversely_append(nums[i, b])
      - if not found:
        reverse whole nums
    """
    a, b, c, d = -1, -1, 0, -1
    for i in range(len(nums)-1, 0, -1):
      if nums[i] > nums[i-1]:
        a = i-1
        d = i
        for j in range(i, len(nums)):
          if nums[j]>nums[a]:
            b = j
          if nums[j]<nums[a]:
            c = j
            break
        break
    
    if d < 0:
      nums.reverse()
    else:
      nums[a], nums[b] = nums[b], nums[a]
      
      left, right = d, len(nums)-1
      while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1