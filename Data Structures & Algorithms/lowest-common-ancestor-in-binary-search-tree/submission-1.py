# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return

            if max(p.val, q.val) > node.val and min(p.val, q.val) < node.val:
                return node

            elif p.val < node.val and q.val < node.val:
                return dfs(node.left)
            
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)

            elif p.val == node.val or q.val == node.val:
                return node

        return dfs(root)
