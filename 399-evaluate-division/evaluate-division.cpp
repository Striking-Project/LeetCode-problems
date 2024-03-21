class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        // Construct the graph
        unordered_map<string, unordered_map<string, double>> graph;
        for (int i = 0; i < equations.size(); ++i) {
            const string& A = equations[i][0];
            const string& B = equations[i][1];
            double value = values[i];
            graph[A][B] = value;
            graph[B][A] = 1.0 / value;
        }
        
        // Perform DFS for each query
        vector<double> results;
        for (const auto& query : queries) {
            string start = query[0];
            string end = query[1];
            if (graph.find(start) == graph.end() || graph.find(end) == graph.end()) {
                results.push_back(-1.0);
            } else {
                unordered_set<string> visited;
                double result = dfs(start, end, graph, visited);
                results.push_back(result);
            }
        }
        
        return results;
    }
    
private:
    double dfs(const string& start, const string& end, unordered_map<string, unordered_map<string, double>>& graph, unordered_set<string>& visited) {
        if (start == end) return 1.0;
        visited.insert(start);
        for (const auto& neighbor : graph[start]) {
            const string& next = neighbor.first;
            if (visited.find(next) == visited.end()) {
                double result = dfs(next, end, graph, visited);
                if (result != -1.0) {
                    return result * neighbor.second;
                }
            }
        }
        return -1.0;
    }
};
