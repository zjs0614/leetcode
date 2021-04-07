class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        counts = [0] * numCourses
        for (a, b) in prerequisites:
            graph[b].append(a)
            counts[a] += 1

        queue = []
        res = []
        for c in range(numCourses):
            if counts[c] == 0:
                queue.append(c)
        
        while len(queue) > 0:
            c = queue.pop(0)
            res.append(c)
            for _c in graph[c]:
                counts[_c] -= 1
                if counts[_c] == 0:
                    queue.append(_c)
        
        if len(res) < numCourses:
            return []
        else:
            return res