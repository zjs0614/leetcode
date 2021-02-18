class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        cur_value = nums[0]
        tmp = self.subsets(nums[1:])
        res = []
        for l in tmp:
            res.append(l)
            n_l = list(l)
            n_l.append(cur_value)
            res.append(n_l)
        return res