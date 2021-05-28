class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Input:
            - s: en lower case, [1, 3*10**4]
            - p: en lower case, [1, 3*10**4]
        Output:
            - List[int]
        
        Analysis:
            - search problem
            - letter_count search
            - sliding window
        
        Solution:
            1) init 2 maps: {letter, count}
                - map1: p
                - map2: current sliding window

            2) sliding window (length: l) move from i to i+1
                - if s[i+l] in map1: decrease map1[s[i+l]]
                - else increase map2[s[i+l]]

                - if s[i] in map2: decrease map2[s[i]]
                - else increase map1[s[i]]

                if map1 and map2 empty, res.add(i)
        """

        res = []

        if len(p) > len(s):
            return res

        map1 = {}
        map2 = {}
        
        letter_set = set()

        # init map1, and letter_set
        for c in p:
            self.addLetterCount(map1, c)
            letter_set.add(c)

        length = len(p)
        for i, c in enumerate(s):
            if i >= length:
                c_drop = s[i-length]
                if c_drop in map2:
                    self.dropLetterCount(map2, c_drop)
                else:
                    self.addLetterCount(map1, c_drop)
            if c in map1:
                self.dropLetterCount(map1, c)
            else:
                self.addLetterCount(map2, c)
            if len(map1) == 0 and len(map2) == 0:
                res.append(i-length+1)
        return res

    def addLetterCount(self, letter_count_map, letter):
        if letter not in letter_count_map:
            letter_count_map[letter] = 1
        else:
            letter_count_map[letter] += 1
        return letter_count_map

    def dropLetterCount(self, letter_count_map, letter):
        if letter in letter_count_map:
            letter_count_map[letter] -= 1
            if letter_count_map[letter] == 0:
                letter_count_map.pop(letter)
        return letter_count_map


