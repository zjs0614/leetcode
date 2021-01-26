class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        max_count = 1
        for index, middle in enumerate(s):
            max_count, result = self.find(index-1, index+1, s, 1, max_count, result)
            max_count, result = self.find(index, index+1, s, 0, max_count, result)
            max_count, result = self.find(index-1, index, s, 0, max_count, result)
        return result

    def find(self, left, right, s, init_count, max_count, result):
        count = init_count
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left, right = left - 1, right + 1
            count += 2
        if count > max_count:
            max_count = count
            result = s[left+1:right]
        return max_count, result