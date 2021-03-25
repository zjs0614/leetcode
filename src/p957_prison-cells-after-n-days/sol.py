class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        num = 0
        for i in cells:
            num = num << 1
            num += i
        
        seen = {}
        flag = True
        i = 0
        while i < n:
            if flag and num in seen:
                i = n - (n-seen[num]) % (i-seen[num])
                flag = False
            else:
                if flag:
                    seen[num] = i
                num = num ^ (num << 2)
                num = num >> 1
                num = num ^ 0b0011111111
                num = num & 0b0001111110
                i += 1
        
        res = [0] * 8
        for i in range(8):
            res[-i-1] = 1 if num & 1 else 0
            num = num >> 1
        return res
        