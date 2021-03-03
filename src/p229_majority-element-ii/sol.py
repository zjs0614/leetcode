class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m, n, cm, cn = 0, 0, 0, 0
        for num in nums:
            if m==num:
                cm += 1
            elif n==num:
                cn += 1
            elif cm <= 0:
                cm = 1
                m = num
            elif cn <= 0:
                cn = 1
                n = num
            else:
                cn -= 1
                cm -= 1
        cm, cn = 0, 0
        for num in nums:
            if num == m:
                cm += 1
            if num == n:
                cn += 1
        res = []
        if cm > len(nums) / 3:
            res.append(m)
        if n != m and cn > len(nums) / 3:
            res.append(n)
        return res