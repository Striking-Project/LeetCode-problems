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
    vector<int> getLeafValues(TreeNode* root) {
        if (!root)
            return {};
        if (!root->left && !root->right)
            return {root->val};
        vector<int> leftLeaves = getLeafValues(root->left);
        vector<int> rightLeaves = getLeafValues(root->right);
        leftLeaves.insert(leftLeaves.end(), rightLeaves.begin(), rightLeaves.end());
        return leftLeaves;
    }
    
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaves1 = getLeafValues(root1);
        vector<int> leaves2 = getLeafValues(root2);
        
        return leaves1 == leaves2;
    }
};