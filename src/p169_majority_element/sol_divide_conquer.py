class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l, v = self.find(nums, 0, len(nums))
        return l
    
    def find(self, nums: List[int], start: int, end: int):
        if start == end - 1:
            return nums[start], 1
        middle = start + int((end - start) / 2)
        l1, v1 = self.find(nums, start, middle)
        l2, v2 = self.find(nums, middle, end)
        if l1 == l2:
            return l1, v1 + v2
        elif v1 > v2:
            return l1, v1 - v2
        elif v2 > v1:
            return l2, v2 - v1
        else:
            return 0, 0