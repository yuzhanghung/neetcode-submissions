# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node, total):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right, total)
            if node.val > high:
                return dfs(node.left, total)
            
            total = (
                dfs(node.left, node.val) + 
                dfs(node.right, node.val))
            
            total += node.val
            return total
        
        return dfs(root, 0)

