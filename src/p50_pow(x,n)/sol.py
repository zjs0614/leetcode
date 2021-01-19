class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return x
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
            
        if n == 1:
            return x
        else:
            extra = x if n % 2 == 1 else 1
            x = self.myPow(x, int(n/2)) 
            return x*x*extra