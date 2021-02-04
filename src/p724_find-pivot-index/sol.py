class Solution:
    def pivotIndex(self, nums) -> int:
        left, right, leftsum, rightsum = 0, len(nums) - 1, 0, 0
        while left < right:
            leftsum, rightsum = leftsum + nums[left], rightsum + nums[right]
            if leftsum == rightsum and left == right - 2:
                return left + 1
            if leftsum < rightsum:
                left += 1
            else:
                right -= 1
        return -1

sol = Solution()
sol.pivotIndex([1,7,3,6,5,6])