class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        root_map = [-1] * n
        children_map = {}
        for edge in edges:
            if not self.merge(edge[0], edge[1], root_map, children_map):
                return False
        if len(children_map) > 1:
            return False
        for i in root_map:
            if i == -1:
                return False
        return True
    
    def merge(self, i, j, root_map, children_map):
        if root_map[i] == -1 and root_map[j] == -1:
            root_map[j] = i
            root_map[i] = i
            if i not in children_map:
                children_map[i] = set()
            children_map[i].add(i)
            children_map[i].add(j)
            return True
        elif root_map[i] >= 0 and root_map[j] >= 0:
            if root_map[i] != root_map[j]:
                old_root, new_root = root_map[j], root_map[i]
                for _j in children_map[old_root]:
                    root_map[_j] = new_root
                    children_map[new_root].add(_j)
                children_map.pop(old_root)
                return True
            else:
                return False
        else:
            if root_map[i] == -1:
                i, j = j, i
            root_map[j] = root_map[i]
            children_map[root_map[i]].add(j)
            return True




class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        root_map = [-1] * n
        children_map = {}
        for edge in edges:
            if not self.merge(edge[0], edge[1], root_map, children_map):
                return False
        if len(children_map) > 1:
            return False
        for i in root_map:
            if i == -1:
                return False
        return True
    
    def merge(self, i, j, root_map, children_map):
        if root_map[i] == -1 and root_map[j] == -1:
            root_map[j] = i
            root_map[i] = i
            if i not in children_map:
                children_map[i] = set()
            children_map[i].add(i)
            children_map[i].add(j)
            return True
        elif root_map[i] >= 0 and root_map[j] >= 0:
            if root_map[i] != root_map[j]:
                old_root, new_root = root_map[j], root_map[i]
                for _j in children_map[old_root]:
                    root_map[_j] = new_root
                    children_map[new_root].add(_j)
                children_map.pop(old_root)
                return True
            else:
                return False
        else:
            if root_map[i] == -1:
                i, j = j, i
            root_map[j] = root_map[i]
            children_map[root_map[i]].add(j)
            return True




