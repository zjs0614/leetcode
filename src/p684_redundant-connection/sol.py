class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root_map = {}
        root_list = {}
        res = []
        for edge in edges:
            i, j = edge[0], edge[1]
            if not self.merge(i, j, root_map, root_list):
                res = [i, j]
        return res
    
    def merge(self, i, j, root_map, root_list):
        if i in root_map and j in root_map:
            if root_map[i] == root_map[j]:
                return False
            new_root = root_map[i]
            old_root = root_map[j]
            for _j in root_list[old_root]:
                root_map[_j] = new_root
                root_list[new_root].add(_j)
            root_list.pop(old_root)
            return True
        elif i not in root_map and j not in root_map:
            root_map[j] = i
            root_map[i] = i
            root_list[i] = set([i, j])
            return True
        else:
            if i not in root_map:
                i, j = j, i
            root = root_map[i]
            root_map[j] = root
            root_list[root].add(j)
            return True