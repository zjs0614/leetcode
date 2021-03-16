class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        div xor bit operation
        '''
        rev = 0
        for num in nums:
            rev = rev ^ num
        div = 1
        while rev & div == 0:
            div = div << 1
        num1, num2 = 0, 0
        for num in nums:
            if num & div == 0:
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num
        return [num1, num2]