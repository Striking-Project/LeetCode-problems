class Solution {
public:
    int numSquares(int n) {
        if (n <= 0) return 0;
        
        // Generate perfect squares
        vector<int> perfectSquares;
        for (int i = 1; i * i <= n; ++i) {
            perfectSquares.push_back(i * i);
        }
        
        // BFS
        queue<pair<int, int>> q;
        q.push({n, 0});
        vector<bool> visited(n + 1, false);
        visited[n] = true;
        
        while (!q.empty()) {
            int num = q.front().first;
            int level = q.front().second;
            q.pop();
            
            for (int square : perfectSquares) {
                int diff = num - square;
                if (diff == 0) {
                    return level + 1;
                } else if (diff > 0 && !visited[diff]) {
                    q.push({diff, level + 1});
                    visited[diff] = true;
                }
            }
        }
        
        return -1; // If no solution found
    }
};