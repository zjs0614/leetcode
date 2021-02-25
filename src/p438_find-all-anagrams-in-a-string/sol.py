class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        (1) len(p) > len(s) or (len(p) == len(s) and p!=s) -> []
        (2) p == s -> [0]
        (3) len(p) < len(s)
            step 1:
                loop each letter of p, build a map:
                    key: [a-z]
                    value: int count
            step 2:
                loop each letter of s, build 

        '''
        res, l_p, l_s = [], len(p), len(s)
        if l_p > l_s:
            return res
        letter_map = {}
        for letter in p:
            if letter in letter_map:
                letter_map[letter] += 1
            else:
                letter_map[letter] = 1
        
        total_count = l_p

        for index, letter in enumerate(s):
            if index >= l_p:
                drop_letter = s[index - l_p]
                if drop_letter in letter_map:
                    letter_map[drop_letter] += 1
                    if letter_map[drop_letter] > 0:
                        total_count += 1
            if letter in letter_map:
                letter_map[letter] -= 1
                if letter_map[letter] >= 0:
                    total_count -= 1
            if total_count == 0:
                res.append(index-l_p+1)
            
        return res









