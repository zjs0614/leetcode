class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        pre_sum = [0] * len(A)
        
        for i, num in enumerate(A):
            pre_sum[i] = num + (pre_sum[i-1] if i > 0 else 0)
        
        l_max = pre_sum[L-1]
        m_max = pre_sum[M-1]
        res = pre_sum[L+M-1]
        for i in range(L+M, len(A)):
            l_max = max(l_max, pre_sum[i-M]-pre_sum[i-L-M])
            m_max = max(m_max, pre_sum[i-L]-pre_sum[i-L-M])
            res = max(res, l_max + pre_sum[i] - pre_sum[i-M], m_max + pre_sum[i] - pre_sum[i-L])
        return res