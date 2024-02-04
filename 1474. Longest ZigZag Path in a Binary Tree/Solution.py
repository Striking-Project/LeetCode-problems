# Definition for a binary tree node.
class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Find the length of the longest ZigZag path in a binary tree.

        Args:
            root (Optional[TreeNode]): The root of the binary tree.

        Returns:
            int: The length of the longest ZigZag path.
        """
        def dfs(node, direction, length):
            nonlocal max_length
            if not node:
                return

            max_length = max(max_length, length)

            if direction == 'left':
                dfs(node.left, 'right', length + 1)
                dfs(node.right, 'left', 1)
            else:
                dfs(node.right, 'left', length + 1)
                dfs(node.left, 'right', 1)

        max_length = 0
        dfs(root, 'left', 0)
        dfs(root, 'right', 0)

        return max_length