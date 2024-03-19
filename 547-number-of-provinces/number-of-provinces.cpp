#include <vector>

class Solution {
public:
    void dfs(std::vector<std::vector<int>>& isConnected, std::vector<bool>& visited, int city) {
        visited[city] = true;
        for (int neighbor = 0; neighbor < isConnected.size(); ++neighbor) {
            if (isConnected[city][neighbor] == 1 && !visited[neighbor]) {
                dfs(isConnected, visited, neighbor);
            }
        }
    }

    int findCircleNum(std::vector<std::vector<int>>& isConnected) {
        int n = isConnected.size();
        std::vector<bool> visited(n, false);
        int provinces = 0;
        for (int city = 0; city < n; ++city) {
            if (!visited[city]) {
                dfs(isConnected, visited, city);
                provinces++;
            }
        }
        return provinces;
    }
};
