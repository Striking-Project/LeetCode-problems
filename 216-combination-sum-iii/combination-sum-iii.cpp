class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> result;
        vector<int> combination;

        function<void(int, int)> backtrack = [&](int start, int remaining) {
            if (combination.size() == k && remaining == 0) {
                result.push_back(combination);
                return;
            }

            if (combination.size() > k || remaining == 0) {
                return;
            }
        
            for (int i = start; i <= 9; ++i) {
                combination.push_back(i);          
                backtrack(i + 1, remaining - i);   
                combination.pop_back();           
            }  
        };

        backtrack(1, n);
        return result;
    }
};