class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        2nd approach:
         step0: loop through nums, and count frequency of each num -> freq_map {}
         step1: build a min heap with size of k
        '''
        if k == 0:
            return []
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] = freq_map[num] + 1
            else:
                freq_map[num] = 1

        res = []
        for key in freq_map:
            if len(res) < k:
                heapq.heappush(res, (freq_map[key], key))
            elif res[0][0] < freq_map[key]:
                heapq.heappop(res)
                heapq.heappush(res, (freq_map[key], key))

        return list(map(lambda x: x[1], res))