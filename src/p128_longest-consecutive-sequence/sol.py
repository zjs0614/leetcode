class Solution:
    def longestConsecutive(self, nums) -> int:
        mem = {}
        res = 1
        for num in nums:
            right_len, left_len = -1, -1
            local_res = 0
            if num + 1 in mem:
                if mem[num + 1] >= 0:
                    right_len = mem[num + 1]
                else:
                    continue
            if num - 1 in mem:
                if mem[num - 1] <= 0:
                    left_len = -mem[num - 1]
                else:
                    continue

            if right_len < 0 and left_len < 0:
                if num not in mem:
                    mem[num] = 0
                
            else:
                if right_len > 0:
                    mem[num] = right_len + 1
                    mem[num + right_len] = -right_len - 1
                    mem.pop(num + 1)
                    local_res += right_len
                elif right_len == 0:
                    mem[num] = 2
                    mem[num + 1] = -2
                    local_res += 1

                if left_len > 0: 
                    mem[num-left_len] = left_len + (1 if num not in mem or mem[num] == 0 else mem[num])
                    if num in mem and mem[num] > 0:
                        mem[num + mem[num] - 1] -= left_len
                    else:
                        mem[num] = -left_len - 1
                    mem.pop(num - 1)
                    local_res += left_len
                elif left_len == 0:
                    mem[num-1] = 1 + (1 if num not in mem or mem[num] == 0 else mem[num])
                    if num in mem and mem[num] > 0:
                        mem[num + mem[num] - 1] -= 1
                    else:
                        mem[num] = -2
                    local_res += 1

                if left_len >=0 and right_len >= 0:
                    mem.pop(num)
            
            local_res += 1
            if local_res > res:
                res = local_res
        return res

sol = Solution()
print(sol.longestConsecutive([-6,8,-5,7,-9,-1,-7,-6,-9,-7,5,7,-1,-8,-8,-2,0]))