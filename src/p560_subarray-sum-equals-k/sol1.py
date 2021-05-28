class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Input:
            - nums: list of nums [-1000, 1000], length: [1, 2*10**4]
            - k: sum of each continuous sub array
        Output:
            - int: num of such subarrays
        
        Analysis:
            - presum with map to store count of pre exist of all sub sum
        
        Examples:
        1)      1, 2, -3, 1, 0, 1, 2    k=2
        presum: 1, 3, 0, 1, 1, 2, 4
        """

        presum = 0
        res = 0
        count = {}
        count[0] = 1

        for num in nums:
            presum += num
            if presum - k in count:
                res += count[presum-k]
            if presum not in count:
                count[presum] = 0
            count[presum] += 1
        return res