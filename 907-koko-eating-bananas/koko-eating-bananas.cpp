class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        auto canFinish = [&](int k) {
            long long hours = 0;
            for (int pile : piles) {
                hours += (pile + k - 1) / k; // Equivalent to math.ceil(pile / k)     
            } 

            return hours <= h;
        };

        int left = 1, right = *max_element(piles.begin(), piles.end());
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canFinish(mid)) {
                right = mid;
            }
            else {
                left = mid + 1;
            }

        } 
        return left;
    }
};