class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for index, temp in enumerate(T):
            while len(stack) > 0 and T[stack[-1]] < temp:
                last_index = stack.pop()
                res[last_index] = index - last_index
            stack.append(index)
        return res