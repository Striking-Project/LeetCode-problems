class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        queue<pair<int, int>> rotten;
        int freshCount = 0;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    ++freshCount;
                } else if (grid[i][j] == 2) {
                    rotten.push({i, j});
                }
            }
        }
        
        if (freshCount == 0) return 0;
        
        int minutes = 0;
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        while (!rotten.empty()) {
            int size = rotten.size();
            
            for (int k = 0; k < size; ++k) {
                int i = rotten.front().first;
                int j = rotten.front().second;
                rotten.pop();
                
                for (const auto& dir : directions) {
                    int ni = i + dir.first;
                    int nj = j + dir.second;
                    
                    if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 1) {
                        grid[ni][nj] = 2;
                        --freshCount;
                        rotten.push({ni, nj});
                    }
                }
            }
            
            ++minutes;
        }
        
        return freshCount == 0 ? minutes - 1 : -1;
    }
};
