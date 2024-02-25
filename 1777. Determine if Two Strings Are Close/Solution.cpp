class Solution {
public:
    bool closeStrings(string word1, string word2) {
        unordered_map<char, int> freq1, freq2;
        for (char ch : word1) freq1[ch]++;
        for (char ch : word2) freq2[ch]++;
        
        vector<int> freq1Values, freq2Values;
        for (auto& kv : freq1) {
            if (!freq2.count(kv.first)) return false;
            freq1Values.push_back(kv.second);
        }
        for (auto& kv : freq2) freq2Values.push_back(kv.second);
        
        sort(freq1Values.begin(), freq1Values.end());
        sort(freq2Values.begin(), freq2Values.end());
        
        return freq1Values == freq2Values;
    }
};
