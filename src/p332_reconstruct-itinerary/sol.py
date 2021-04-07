class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        for ticket in tickets:
            origin, destination = ticket[0], ticket[1]
            if origin not in graph:
                graph[origin] = {}
            if destination not in graph[origin]:
                graph[origin][destination] = 0
            graph[origin][destination] += 1
        
        flight_count = 0
        cur_pos = "JFK"

        res = self.dfs(cur_pos, graph, [cur_pos], flight_count, len(tickets))
        if res is None:
            return []
        else:
            return res

    def dfs(self, cur_pos, graph, res, flight_count, total_count):
        if flight_count == total_count:
            return res

        next_pos_list = set()
        if cur_pos in graph:
            for destination in graph[cur_pos]:
                if graph[cur_pos][destination] > 0:
                    next_pos_list.add(destination)
        
        if len(next_pos_list) == 0:
            return None

        next_pos_list = sorted(next_pos_list)
        for next_pos in next_pos_list:
            graph[cur_pos][next_pos] -= 1
            res.append(next_pos)
            _res = self.dfs(next_pos, graph, res, flight_count+1, total_count)
            if _res is not None:
                return _res
            res.pop()
            graph[cur_pos][next_pos] += 1
            
        return None


