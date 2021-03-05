class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        count = 1
        while n >= 4:
            res.append(count)
            res.append(-count)
            count += 1
            n -= 2
        if n == 3:
            res.append(count)
            res.append(count+1)
            res.append(-count-count-1)
        elif n == 2:
            res.append(count)
            res.append(-count)
        elif n == 1:
            res.append(0)
        return res