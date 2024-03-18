class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
            int n = rooms.size();
            unordered_set<int> visited;

            function<void(int)> dfs = [&](int room) {
                visited.insert(room);
                for (int key : rooms[room]) {
                    if (visited.find(key) == visited.end()) {
                        dfs(key);
                    }
                }
            };

            dfs(0);
            
            return visited.size() == n;
    }
};