class Solution {
public:
    string decodeString(string s) {
        stack<int> counts;
        stack<string> strings;
        string current_string;
        int current_sum = 0;

        for (char c : s) {
            if (isdigit(c)) {
                current_sum = current_sum * 10 + (c - '0'); 
            } else if (c == '[') {
                counts.push(current_sum);
                strings.push(current_string);
                current_sum = 0;
                current_string = "";
            } else if (c == ']') {
                int repeat_count = counts.top();
                counts.pop();
                string prev_string = strings.top();
                strings.pop();
                for (int i = 0; i < repeat_count; i++) {
                    prev_string += current_string;
                }
                current_string = prev_string;
            } else {
                current_string += c;
            }
        }
        return current_string;
    }
};