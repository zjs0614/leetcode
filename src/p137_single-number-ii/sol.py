class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        - Problem Definition:
            0) A search problem
            1) target must exist and only appear once
            2) target is the minority
            3) all other numbers appear equal number of times = 3
            4) list is not ordered
            5) 1 <= length <= 3 * 10_000
            6) all integers
        - Solution Constraints:
            0) linear time complexity
            1) no extra memory
        - Test cases:
            0) [1] -> 1
            1) [0,1,0,0] -> 1
        - Solutionn:
            bit operation
        '''
        once, twice = 0, 0
        for num in nums:
            once = once ^ num & ~ twice
            twice = twice ^ num & ~ once
        return once