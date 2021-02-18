class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDictMap = {}
        for word in wordDict:
            letter = word[0]
            if letter in wordDictMap:
                wordDictMap[letter].append(word)
            else:
                wordDictMap[letter] = [word]
        return self.find(s, wordDictMap, set())
    
    def find(self, s, wordDictMap, failed):
        if s == "":
            return True
        elif len(s) in failed:
            return False

        letter = s[0]
        if letter in wordDictMap:
            wordDict = wordDictMap[letter]
            for word in wordDict:
                if len(word) <= len(s) and s[0:len(word)] == word:
                    check = self.find(s[len(word):], wordDictMap, failed)
                    if check:
                        return True
        failed.add(len(s))
        return False