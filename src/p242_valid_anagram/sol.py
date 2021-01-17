class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s is not None and t is not None and len(s) == len(t):
            str_count = [0] * 26
            for index, i in enumerate(s):
                str_count[ord(i) - ord('a')] += 1
                str_count[ord(t[index]) - ord('a')] -= 1
            for i in str_count:
                if i != 0:
                    return False
            return True
        return False