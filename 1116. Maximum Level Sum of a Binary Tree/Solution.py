# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float('-inf')
        result_level = 0
        current_level = 1

        queue = deque([root])

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                current = queue.popleft()
                level_sum += current.val

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            if level_sum > max_sum:
                max_sum = level_sum
                result_level = current_level

            current_level += 1

        return result_level
