class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.find(0, 0, n, result, "")
        return result

    def find(self, left: int, right: int, size: int, result: List, currentList: str):
        if right > left or left > size or right > size:
            return
        if left == right == size:
            result.append(currentList)
            return
        self.find(left + 1, right, size, result, currentList + "(")
        self.find(left, right + 1, size, result, currentList + ")")