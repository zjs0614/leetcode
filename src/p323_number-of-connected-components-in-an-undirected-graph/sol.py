class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        root_map = list(range(n))
        children_map = {}
        for i in range(n):
            children_map[i] = set([i])

        for edge in edges:
            self.merge(edge[0], edge[1], root_map, children_map)
            
        return len(children_map)
    
    def merge(self, i, j, root_map, children_map):
        if root_map[i] == -1 and root_map[j] == -1:
            root_map[j] = i
            root_map[i] = i
            if i not in children_map:
                children_map[i] = set()
            children_map[i].add(i)
            children_map[i].add(j)
        elif root_map[i] >= 0 and root_map[j] >= 0:
            if root_map[i] != root_map[j]:
                old_root, new_root = root_map[j], root_map[i]
                for _j in children_map[old_root]:
                    root_map[_j] = new_root
                    children_map[new_root].add(_j)
                children_map.pop(old_root)
        else:
            if root_map[i] == -1:
                i, j = j, i
            root_map[j] = root_map[i]
            children_map[root_map[i]].add(j)