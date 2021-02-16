class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.getCombination(nums, len(nums), set())

    def getCombination(self, nums, count, exists):
        res = []
        for num in nums:
            if num not in exists:
                if count > 1:
                    exists.add(num)
                    tmp = self.getCombination(nums, count-1, exists)
                    exists.remove(num)
                    for i in tmp:
                        i.append(num)
                    res.extend(tmp)
                elif count == 1:
                    res.append([num])
        return res