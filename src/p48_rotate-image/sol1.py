class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    """
    Args:
      - matrix: List[List[int]], nxn matrix, n: [1, 20], value: [-1000, 1000]
    Returns:
      - no return
    
    Restriction:
      - inplace update matrix, donn't create new 2D matrix
    
    Analysis:
      - Transition Functions:
        - matrix: m, nxn size:
          for item at m[i][j]:
            new_i = j
            new_j = n-i-1
      - layer by layer: 0,0 -> 1,1 -> 2,2 -> .. -> int((n+1)/2)-1, int((n+1)/2)-1
        - for each layer ixi:
          loop from i,i to i, n-i-1:
            rotate update i,i: 4 times
    """
    n = len(matrix)
    for i in range(0, int((n+1)/2)):
      for j in range(i, n-i-1):
        temp = matrix[i][j]
        cur_i, cur_j = i, j
        for _ in range(0, 4):
          next_i = cur_j
          next_j = n-cur_i-1
          temp, matrix[next_i][next_j] = matrix[next_i][next_j], temp
          cur_i, cur_j = next_i, next_j
