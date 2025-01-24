class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        vector<string> digitToChar = {
            "",    // 0 (not used)
            "",    // 1 (not used)
            "abc", // 2
            "def", // 3
            "ghi", // 4
            "jkl", // 5
            "mno", // 6
            "pqrs",// 7
            "tuv", // 8
            "wxyz" // 9
        };

        vector<string> result; 
        string currentCombination; 

        
        function<void(int)> backtrack = [&](int index) {
            if (index == digits.size()) {
                result.push_back(currentCombination);
                return;
            }

            string letters = digitToChar[digits[index] - '0'];
            for (char letter : letters) {
                currentCombination.push_back(letter); 
                backtrack(index + 1);
                currentCombination.pop_back(); 
            }
        };

        backtrack(0); 
        return result;
    }
};