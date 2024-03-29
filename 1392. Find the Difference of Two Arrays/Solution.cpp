#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<std::vector<int>> findDifference(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_set<int> set1(nums1.begin(), nums1.end());
        std::unordered_set<int> set2(nums2.begin(), nums2.end());
        
        std::vector<int> difference1;
        std::vector<int> difference2;
        
        for (int num : set1) {
            if (set2.find(num) == set2.end()) {
                difference1.push_back(num);
            }
        }
        
        for (int num : set2) {
            if (set1.find(num) == set1.end()) {
                difference2.push_back(num);
            }
        }
        
        return {difference1, difference2};
    }
};
