/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long, int> prefix_sum_map;
        prefix_sum_map[0] = 1;
        return dfs(root, 0LL, (long long)targetSum, prefix_sum_map);
    }

private:
    int dfs(TreeNode* node, long long current_sum, long long target_sum, unordered_map<long long, int>& prefix_sum_map) {
        if (!node) return 0;
        
        current_sum += node->val;
        int count = prefix_sum_map[current_sum - target_sum];
        
        prefix_sum_map[current_sum]++;
        
        count += dfs(node->left, current_sum, target_sum, prefix_sum_map);
        count += dfs(node->right, current_sum, target_sum, prefix_sum_map);
        
        prefix_sum_map[current_sum]--;
        
        return count;
    }
};
