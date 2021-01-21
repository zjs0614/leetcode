class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        return self.find(x, 1, x)

    def find(self, x: int, v1: int, v2: int):
        if v2 == v1:
            return v1
        middle = v1 + int((v2-v1) / 2)
        v = middle * middle
        if v == x:
            return middle
        elif v > x:
            return self.find(x, v1, middle)
        else:
            if middle == v2:
                return v2
            if middle == v1:
                v2 = v2 - 1
            return self.find(x, middle, v2) 