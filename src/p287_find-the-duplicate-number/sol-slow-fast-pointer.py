class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) <= 2:
            return nums[0]

        slow, fast = nums[0], nums[nums[0]]
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
        return nums[fast]


