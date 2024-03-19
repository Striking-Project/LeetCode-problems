class Solution:
    def dfs(self, isConnected, visited, city):
        visited[city] = True
        for neighbor, connected in enumerate(isConnected[city]):
            if connected == 1 and not visited[neighbor]:
                self.dfs(isConnected, visited, neighbor)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        for city in range(n):
            if not visited[city]:
                self.dfs(isConnected, visited, city)
                provinces += 1
        return provinces
