class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if len(A) < len(B):
            return self.find(A, B)
        else:
            return self.find(B, A)
    
    def find(self, A, B):
        a_left, a_right = len(A)-1, len(A)-1
        b_left, b_right = 0, 0
        res = 0
        while b_left < len(B) and a_left >= 0:
            count = 0
            index = 0
            while index <= a_right - a_left:
                if A[a_left+index] != B[b_left+index]:
                    if count > res:
                        res = count
                    count = 0
                else:
                    count += 1
                index += 1
            if count > res:
                res = count
            if a_left > 0:
                a_left -= 1
                b_right += 1
            elif b_right < len(B) - 1:
                b_left += 1
                b_right += 1
            else:
                b_left += 1
                a_right -= 1
        return res

