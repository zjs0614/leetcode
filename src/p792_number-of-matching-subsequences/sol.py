class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        letter_bucket = [[] for _ in range(26)]
        for word in words:
            letter_bucket[ord(word[0])-ord('a')].append(word)
        res = 0
        for letter in S:
            res_words = letter_bucket[ord(letter)-ord('a')]
            letter_bucket[ord(letter)-ord('a')] = []
            for word in res_words:
                new_word = word[1:]
                if new_word == "":
                    res += 1
                else:
                    letter_bucket[ord(new_word[0])-ord('a')].append(new_word)
        return res
