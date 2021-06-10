class Solution:
  def partition(self, s: str) -> List[List[str]]:
    dp = self.getAllPalindromeSubStr(s)
    return self.getPartitions(s, dp, 0)


  def getPartitions(self, s, dp, start):
    res = []
    for i in range(start, len(s)):
      if dp[start][i] == 1:
        if i == len(s) - 1:
          res.append([s[start:i+1]])
        else:
          sub_partitions = self.getPartitions(s, dp, i+1)
          if sub_partitions:
            for sub_partition in sub_partitions:
              res.append([s[start:i+1]] + sub_partition)
    return res

  def getAllPalindromeSubStr(self, s):
    size = len(s)
    dp = [[0] * size for _ in range(size)]
    for i in range(size):
      left, right = i, i
      while left >= 0 and right < size:
        if s[left] == s[right]:
          dp[left][right] = 1
          left -= 1
          right += 1
        else:
          break
      if i < size - 1 and s[i] == s[i+1]:
        left, right = i, i+1
        while left >= 0 and right < size:
          if s[left] == s[right]:
            dp[left][right] = 1
            left -= 1
            right += 1
          else:
            break
    return dp