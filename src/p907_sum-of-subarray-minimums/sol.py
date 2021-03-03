class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        right_covers = [1] * len(arr)
        i = 0
        while i <= len(arr):
            while len(stack) > 0 and (i == len(arr) or arr[i] < arr[stack[-1]]):
                last_index = stack.pop()
                right_covers[last_index] = i - last_index
            stack.append(i)
            i += 1

        stack = []
        left_covers = [1] * len(arr)
        i = len(arr) - 1
        while i >= -1:
            while len(stack) > 0 and (i == -1 or arr[i] <= arr[stack[-1]]):
                last_index = stack.pop()
                left_covers[last_index] = last_index - i
            stack.append(i)
            i -= 1

        res = 0
        for i, num in enumerate(arr):
            res += num * left_covers[i] * right_covers[i]

        return res % (10 ** 9 + 7)