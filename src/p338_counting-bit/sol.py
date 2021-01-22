class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * num
        for i in range(1, len(num)):
            