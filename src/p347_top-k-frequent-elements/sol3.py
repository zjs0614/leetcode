class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        3rd approach:
         step0: loop through nums, and count frequency of each num -> freq_map {}
         step1: create array A with size n + 1, A[i] is the num with frequency of i
         step2: loop backward of A, find first K items with A[i] > 0
        '''
        if k == 0:
            return []
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] = freq_map[num] + 1
            else:
                freq_map[num] = 1
        buckets = [None] * len(nums)

        for key in freq_map:
            if buckets[freq_map[key]-1] is None:
                buckets[freq_map[key]-1] = [key]
            else:
                buckets[freq_map[key]-1].append(key)

        res, index = [], len(buckets)-1
        while len(res) < k and index >= 0:
            if buckets[index] is not None:
                res.extend(buckets[index])
            index -= 1
        return res