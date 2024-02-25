class Solution {
public:
    bool closeStrings(string word1, string word2) {
        unordered_map<char, int> freq1, freq2;
        for (char ch : word1) freq1[ch]++;
        for (char ch : word2) freq2[ch]++;
        
        set<char> chars1(word1.begin(), word1.end()), chars2(word2.begin(), word2.end());
        
        vector<int> freq1Values, freq2Values;
        for (auto& kv : freq1) freq1Values.push_back(kv.second);
        for (auto& kv : freq2) freq2Values.push_back(kv.second);
        
        sort(freq1Values.begin(), freq1Values.end());
        sort(freq2Values.begin(), freq2Values.end());
        
        return chars1 == chars2 && freq1Values == freq2Values;
    }
};
