import string
class Solution:
    def hashCode(self, word):
        letter_count = {}
        for letter in word:
            if letter in letter_count:
                letter_count[letter] = letter_count[letter] + 1
            else:
                letter_count[letter] = 1
        res = ""
        for letter in list(string.ascii_lowercase):
            if letter in letter_count:
                res = res + (letter + str(letter_count[letter]))
        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for word in strs:
            hash_code = self.hashCode(word)
            if hash_code in anagram_map:
                anagram_map[hash_code].append(word)
            else:
                anagram_map[hash_code] = [word]
        res = []
        for _ in anagram_map:
            res.append(anagram_map[_])
        return res