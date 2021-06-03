class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    """
    Analysis:
      - search problem
      - dp[i] = (s[i:j] in wordDict) and dp[j]
    """
    word_dict = set(wordDict)
    size = len(s)
    dp = [False] * size

    for i in range(size-1, -1, -1):
      for word in word_dict:
        word_length = len(word)
        if i + word_length == size and s[i:size] == word:
          dp[i] = True
          break
        elif i + word_length < size and s[i:i+word_length] == word and dp[i+word_length]:
          dp[i] = True
          break
    return dp[0]