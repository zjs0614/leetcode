class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        cases:
        1) [0,1][1,2] -> True
        2) [0,1][1,0] -> False
        3) [0,1][1,0][2,1] -> False
        4) [0,1][1,0][2,1][0,2] -> False
        Circle exists then return False
        '''
        '''
        Kahn
        '''
        indgree = {}
        diagram = {}
        for index, pair in enumerate(prerequisites):
            if pair[0] in indgree:
                indgree[pair[0]] += 1
            else:
                indgree[pair[0]] = 1
            if pair[1] not in indgree:
                indgree[pair[1]] = 0
            if pair[1] in diagram:
                diagram[pair[1]].add(pair[0])
            else:
                diagram[pair[1]] = set([pair[0]])
        queue = []
        for node in indgree:
            if indgree[node] == 0:
                queue.append(node)
        res = len(indgree)
        while len(queue) > 0:
            n1 = queue.pop(0)
            res -= 1
            if n1 in diagram:
                for n2 in diagram[n1]:
                    indgree[n2] -= 1
                    if indgree[n2] == 0:
                        queue.append(n2)
        return res == 0





