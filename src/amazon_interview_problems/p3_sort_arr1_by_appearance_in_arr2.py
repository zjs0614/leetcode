class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num_count = list(range(0, 1001))
        for i, num in enumerate(arr2):
            num_count[num] = -len(arr2)+i
        return sorted(arr1, key=lambda x: num_count[x])
