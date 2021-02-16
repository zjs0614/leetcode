class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.getCombination(candidates, target)
    
    def getCombination(self, nums, target):
        res = []
        for index, num in enumerate(nums):
            if num > target:
                break
            elif num == target:
                res.append([num])
            else:
                tmp = self.combinationSum(nums[index:], target - num)
                for i in tmp:
                    i.append(num)
                res.extend(tmp)
        return res
