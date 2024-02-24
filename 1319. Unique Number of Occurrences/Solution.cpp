class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        std::unordered_map<int, int> freq;
        for (int num : arr) {
            freq[num]++;
        }

        std::unordered_set<int> countSet;
        for (const auto& kv : freq) {
            if (countSet.find(kv.second) != countSet.end()) {
                return false;
            }
            countSet.insert(kv.second);
        }        
        return true;
    }
};