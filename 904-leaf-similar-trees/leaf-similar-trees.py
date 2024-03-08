# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf_values(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return get_leaf_values(root.left) + get_leaf_values(root.right)
        
        leaves1 = get_leaf_values(root1)
        leaves2 = get_leaf_values(root2)
        
        return leaves1 == leaves2
