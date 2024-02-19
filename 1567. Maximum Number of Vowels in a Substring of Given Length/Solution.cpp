class Solution {
public:
    int maxVowels(string s, int k) {
        int maxVowelCount = 0;
        int currentVowelCount = 0;
        bool vowels[26] = {false};
        vowels['a' - 'a'] = true;
        vowels['e' - 'a'] = true;
        vowels['i' - 'a'] = true;
        vowels['o' - 'a'] = true;
        vowels['u' - 'a'] = true;

        for (int i = 0; i < k; ++i) {
            if (vowels[s[i] - 'a']) {
                currentVowelCount ++;     
            }
        }
        maxVowelCount = currentVowelCount;

        for (int i = k; i < s.length(); ++i) {
            if (vowels[s[i] - 'a']) {
                currentVowelCount ++;     
            }
            if (vowels[s[i - k] - 'a']) {
                currentVowelCount --;     
            }
            maxVowelCount = max(maxVowelCount, currentVowelCount);
        }    
        return maxVowelCount;
    }
};