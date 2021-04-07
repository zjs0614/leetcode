class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        relations = [set() for _ in range(n)]
        for edge in edges:
            relations[edge[0]].add(edge[1])
            relations[edge[1]].add(edge[0])

        if len(edges) == 0:
            return [0]
            
        nodes = []
        for i, neighbors in enumerate(relations):
            if len(neighbors) == 1:
                nodes.append(i)
        return self.find_common_root(nodes, relations)
    
    def find_common_root(self, nodes, relations):
        
        if len(nodes) == 1:
            return nodes
        if len(nodes) == 2 and nodes[1] in relations[nodes[0]]:
            return nodes

        roots = set()
        for node in nodes:
            for neighbor in relations[node]:
                relations[neighbor].remove(node)
                if len(relations[neighbor]) == 1:
                    roots.add(neighbor)
        return self.find_common_root(list(roots), relations)
