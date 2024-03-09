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
    int goodNodes(TreeNode* root) {
        return dfs(root, INT_MIN);
    }
    
    int dfs(TreeNode* node, int max_val);
};

int Solution::dfs(TreeNode* node, int max_val) {
    if (!node) {
        return 0;
    }
    
    int count = (node->val >= max_val) ? 1 : 0;
    max_val = max(max_val, node->val);
    int left_count = dfs(node->left, max_val);
    int right_count = dfs(node->right, max_val);
    
    return count + left_count + right_count;
}