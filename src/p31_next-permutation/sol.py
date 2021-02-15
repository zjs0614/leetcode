class Solution:
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Cases:
        1) 1, 2, 3, 4 -> 1, 2, 4, 3
        2) 1, 2, 8, 7, 3, 5, 4
        3) 1, 4, 6, 2, 3, 7, 8
        4) 8, 7, 6, 3, 4, 5, 2, 1 -> 8, 7, 6, 3, 5, 1, 2, 4 
        5) 8, 7, 6, 3, 2, 5, 4, 1 -> 8, 7, 6, 3, 4, 1, 2, 5 

        loop from len(nums)-2 to 0, find the first position i, where nums[i] < nums[i+1]
            if i found:
                reverse nums in range i+1 to len(nums) - 1
                find the smallest number in the reversed range that bigger than nums[i] at j
                replace nums[i] with nums[j]
            else
                reverse whole nums
        '''
        if len(nums) <= 1:
            return nums
        i = len(nums) - 2
        while i >= 0:
            if nums[i] >= nums[i+1]:
                i -= 1
                continue
            else:
                self.reverse(nums, i+1, len(nums)-1)
                j = i+1
                while j < len(nums)-1:
                    if nums[j] > nums[i]:
                        break;
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
                return
        self.reverse(nums, 0, len(nums) - 1)



