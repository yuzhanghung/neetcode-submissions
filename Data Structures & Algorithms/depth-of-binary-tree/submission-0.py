class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        depth = max(depth, self.maxDepth(root.left))
        depth = max(depth, self.maxDepth(root.right))

        return depth + 1