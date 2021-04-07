class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = {}
        counts = {}
        total_count = 0
        for seq in seqs:
            for i in range(len(seq)):
                b = seq[i]
                if b not in counts:
                    counts[b] = 0
                if i > 0:
                    a = seq[i-1]
                    if a not in graph:
                        graph[a] = []
                    graph[a].append(b)
                    if a not in counts:
                        counts[a] = 0
                    counts[b] += 1
                    total_count += 1
        
        queue = []
        for item in counts:
            if counts[item] == 0:
                queue.append(item)
        index = 0
        while len(queue) > 0:
            if index >= len(org):
                return False
            if len(queue) > 1:
                return False
            item = queue.pop(0)
            if item != org[index]:
                return False
            index += 1
            if item in graph:
                for _item in graph[item]:
                    counts[_item] -= 1
                    total_count -= 1
                    if counts[_item] == 0:
                        queue.append(_item)
        
        return index == len(org) and total_count == 0




