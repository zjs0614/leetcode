class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        accum, mem, res = 0, {}, 0
        for num in A:
            accum = (accum + num) % K
            if accum == 0:
                res += 1
            if accum in mem:
                res += mem[accum]
                mem[accum] += 1
            else:
                mem[accum] = 1
        return res