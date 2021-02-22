class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Union Find
        '''
        head_map = {}
        for index, equation in enumerate(equations):
            a, b = equation[0], equation[1]
            a, w1 = self.find_root(a, head_map, True)
            b, w2 = self.find_root(b, head_map, True)
            if a != b:
                head_map[b] = (a, values[index] * w1 / w2)
                head_map[a] = (a, 1)
        
        res = []
        for index, query in enumerate(queries):
            a, b = query[0], query[1]
            a, w1 = self.find_root(a, head_map, False)
            b, w2 = self.find_root(b, head_map, False)
            if a is not None and b is not None and a == b:
                res.append(w2 / w1)
            else:
                res.append(-1)
        return res

    def find_root(self, node, head_map, insert):
        weight = 1
        original_node = node
        while node in head_map:
            if node == head_map[node][0]:
                return node, weight
            node, weight = head_map[node][0], weight * head_map[node][1]
        if node != original_node:
            head_map[original_node] = (node, weight)
        elif not insert:
            node = None
        return node, weight
