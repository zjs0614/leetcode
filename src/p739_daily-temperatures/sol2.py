class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Input:
            [2,3,4,1,8,6,5]
        Output:
            [1,1,2,1,0,0,0]
        Monotone Stack Problem
        """
        size = len(temperatures)
        post_max = []
        res = [0] * size

        for i in range(size-1, -1, -1):
            while len(post_max) > 0 and temperatures[post_max[-1]] <= temperatures[i]:
                post_max.pop()
            res[i] = 0 if len(post_max) == 0 else post_max[-1] - i
            post_max.append(i)

        return res