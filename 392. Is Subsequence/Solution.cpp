class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sIndex = 0, tIndex = 0;
        int sLen = s.length(), tLen = t.length();

        while (sIndex < sLen && tIndex < tLen) {
            if (s[sIndex] == t[tIndex]) {
                sIndex++;
            }
            tIndex++;
        }

        return sIndex == sLen;
    }
};