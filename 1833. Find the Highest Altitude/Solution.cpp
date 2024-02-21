class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int max_altitude = 0;
        int current_altitude = 0;
        
        vector<int> prefix_sum(gain.size() + 1, 0);
        for (int i = 1; i <= gain.size(); ++i) {
            prefix_sum[i] = prefix_sum[i - 1] + gain[i - 1];
        }
        
        for (int altitude : prefix_sum) {
            max_altitude = max(max_altitude, altitude);
        }
        
        return max_altitude;
    }
};