class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        1st approach:
         step0: loop through nums, and count frequency of each num -> freq_map {}
         step1: loop freq_map k times, to pick key have the biggest frequency number, and delete the key from the map
         step2: return result
        '''
        if k == 0:
            return []
        res = []
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] = freq_map[num] + 1
            else:
                freq_map[num] = 1
        for i in range(k):
            max_count, max_count_key = 0, 0
            for key in freq_map:
                if freq_map[key] > max_count:
                    max_count = freq_map[key]
                    max_count_key = key
            res.append(max_count_key)
            freq_map.pop(max_count_key)
        return res