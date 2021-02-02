class Solution:

    def findRoot(self, cities, ci):
        if ci == cities[ci]:
            return ci
        else:
            return self.findRoot(cities, cities[ci])
    
    def overrideRoot(self, cities, ci, root):
        if ci != cities[ci]:
            self.overrideRoot(cities, cities[ci], root)
        cities[ci] = root


    def findCircleNum(self, isConnected) -> int:
        cities = [x for x in range(len(isConnected))]
        for i, row in enumerate(isConnected):
            for j, city in enumerate(row[i+1:]):
                ci = j + i + 1
                if city == 1:
                    if cities[ci] != ci:
                        root = self.findRoot(cities, i)
                        self.overrideRoot(cities, cities[ci], root)
                        cities[ci] = root
                    else:
                        cities[ci] = cities[i]

        res = 0
        for index, city in enumerate(cities):
            if city == index:
                res += 1
        return res