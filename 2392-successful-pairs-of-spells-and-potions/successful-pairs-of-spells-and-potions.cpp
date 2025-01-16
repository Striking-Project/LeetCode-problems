class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
       sort(potions.begin(), potions.end());
       int m = potions.size();
       vector<int> result;

       for (int spell : spells){
        long long required_potion = (success + spell - 1) / spell;

        int left = 0, right = m - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (potions[mid] < required_potion) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }  
        int count = m - left;
        result.push_back(count);
       }    
       return result;
    }
};