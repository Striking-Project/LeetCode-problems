from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        # Construct the graph
        for (Ai, Bi), value in zip(equations, values):
            graph[Ai][Bi] = value
            graph[Bi][Ai] = 1 / value
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result
            
            return -1.0
        
        results = []
        for query in queries:
            result = dfs(query[0], query[1], set())
            results.append(result)
        
        return results
