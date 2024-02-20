class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int left = 0;
        int max_ones = 0;
        int zero_count = 0;
        int max_window = 0;
        
        for (int right = 0; right < nums.size(); ++right) {
            if (nums[right] == 0) {
                zero_count++;
            }
            
            while (zero_count > k) {
                if (nums[left] == 0) {
                    zero_count--;
                }
                left++;
            }
            
            max_window = max(max_window, right - left + 1);
        }
        
        return max_window;
    }
};
