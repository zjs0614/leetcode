class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        local_count, res, sign = 1, 1, 0
        for i, num in enumerate(arr[1:]):
            pre_num = arr[i]
            if num == pre_num:
                local_count = 1
                sign = 0
            elif sign != 0:
                if (num > pre_num and sign > 0) or (num < pre_num and sign < 0):
                    local_count += 1
                    sign = -sign
                else:
                    local_count = 2
                    sign = 1 if num < pre_num else -1
            else:
                local_count += 1
                sign = 1 if num < pre_num else -1
            
            if local_count > res:
                res = local_count

        return res