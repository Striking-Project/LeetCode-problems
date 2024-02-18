class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double windowSum = accumulate(nums.begin(), nums.begin() + k, 0.0);
        double maxSum = windowSum;

        for (int i = k; i < nums.size(); ++i){
            windowSum += nums[i] - nums[i - k];
            maxSum = max(maxSum, windowSum); 
        }

        return maxSum / k;
    }
};