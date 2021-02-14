class Solution:
    def reverse(self, x: int) -> int:
        res, neg, x = 0, x<0, x if x > 0 else -x
        v_min, v_max = - (2 ** 31), 2 ** 31 - 1
        while x != 0:
            if res != 0:
                res *= 10
            res += x % 10
            x = int(x / 10)
            if (res > v_max and not neg) or (-res < v_min and neg):
                return 0
        return -res if neg else res
