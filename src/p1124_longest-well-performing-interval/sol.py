class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res, accum, mem = 0, 0, {}
        for index, hour in enumerate(hours):
            accum = accum + 1 if hour > 8 else accum - 1
            if accum > 0:
                res = index + 1
            else:
                if (accum - 1) in mem and index - mem[accum - 1] > res:
                    res = index - mem[accum - 1]
            if accum not in mem:
                mem[accum] = index
        return res
            