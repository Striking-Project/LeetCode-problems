#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int rows = maze.size();
        int cols = maze[0].size();
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int entrance_row = entrance[0];
        int entrance_col = entrance[1];
        
        queue<tuple<int, int, int>> q;  // (row, col, steps)
        q.push({entrance_row, entrance_col, 0});
        maze[entrance_row][entrance_col] = '#';  // Mark entrance as visited
        
        while (!q.empty()) {
            int row, col, steps;
            tie(row, col, steps) = q.front();
            q.pop();
            
            if ((row != entrance_row || col != entrance_col) && (row == 0 || row == rows - 1 || col == 0 || col == cols - 1)) {
                return steps;
            }
            
            for (auto& [dr, dc] : directions) {
                int r = row + dr;
                int c = col + dc;
                if (r >= 0 && r < rows && c >= 0 && c < cols && maze[r][c] == '.') {
                    maze[r][c] = '#';  // Mark cell as visited
                    q.push({r, c, steps + 1});
                }
            }
        }
        
        return -1;
    }
};
