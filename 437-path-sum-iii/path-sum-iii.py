# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, current_sum, target_sum, prefix_sum_map):
            if not node:
                return 0
            
            current_sum += node.val
            count = prefix_sum_map[current_sum - target_sum]
            
            prefix_sum_map[current_sum] += 1
            
            count += dfs(node.left, current_sum, target_sum, prefix_sum_map)
            count += dfs(node.right, current_sum, target_sum, prefix_sum_map)
            
            prefix_sum_map[current_sum] -= 1
            
            return count
        
        prefix_sum_map = defaultdict(int)
        prefix_sum_map[0] = 1  
                    
        return dfs(root, 0, targetSum, prefix_sum_map)
