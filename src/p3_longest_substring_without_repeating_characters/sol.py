class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        records = {}

        result = 0
        start = 0
        end = 0

        for index, char in enumerate(s):
            end = index
            if char in records:
                new_start = records[char] + 1
                for char_remove in s[start:new_start]:
                    records.pop(char_remove)
                start = new_start

            records[char] = index

            if end - start + 1 > result:
                result = end - start + 1

        return result