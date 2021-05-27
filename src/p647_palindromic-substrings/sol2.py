class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Input: string [1, 1000] lowercase en only
            e.g: "abcaabbccbb"
        Ouput: num of palindromic substrings

            - case1: len: len(s)
            - case2: start from 1: xxaxx
            - case3: start from 2: xxaaxx

        Sol:
            - search problem
            - loop from 1..n,
                - check case 2 and case 3 separately
            
            O(n * 2n)
        """
        res = 0

        size = len(s)

        for i in range(0, size):
            res += 1
            left, right = i-1, i+1
            res += self.countSubPalindromicString(i-1, i+1, s)
            if i+1 < size and s[i+1] == s[i]:
                res += 1
                res += self.countSubPalindromicString(i-1, i+2, s)
        return res

    def countSubPalindromicString(self, left, right, s):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res













