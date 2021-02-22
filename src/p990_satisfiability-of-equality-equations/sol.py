class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        head_map = {}
        for equation in equations:
            if equation[1] == "=":
                a, b = self.find_head(equation[0], head_map), self.find_head(equation[3], head_map)
                if a != b:
                    head_map[b] = a
        
        for equation in equations:
            isEqual = equation[1] == "="
            a, b = self.find_head(equation[0], head_map), self.find_head(equation[3], head_map)
            if (a != b and isEqual) or (a == b and not isEqual):
                return False
        return True
        
    def find_head(self, x, head_map):
        original = x
        while x in head_map:
            if head_map[x] == x:
                break
            x = head_map[x]
        head_map[original] = x
        return x