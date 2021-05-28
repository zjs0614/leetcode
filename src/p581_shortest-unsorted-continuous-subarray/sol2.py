class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Input:
            - nums: list of nums [-10**5, 10**5], 1 <= length <= 10**4
        Output:
            - int: min length of continuous subarray to be sort to make whole list sorted (ascending)
        
        e.g.
            - [2,6,4,8,10,9,15] -> [2,*4,6,8,9,10*,15] => 5
        
        Solution:
            - Task interpretation: Find boundary
                - left: has num less than num[left] whose index > left
                - right: has num bigger than num[right] whose index < right

            - Data Structure
              post_min array, keep the index of the min num on the right
        """
        size = len(nums)
        post_min = size - 1
        left, right = size, -1
        for i in range(size-2, -1, -1):
            if nums[i] <= nums[post_min]:
                post_min = i
            else:
                left = min(left, i)
        if left < size:
            pre_max = 0
            for i in range(1, size):
                if nums[i] >= nums[pre_max]:
                    pre_max = i
                else:
                    right = max(right, i)
        return right - left + 1 if right >= 0 else 0



