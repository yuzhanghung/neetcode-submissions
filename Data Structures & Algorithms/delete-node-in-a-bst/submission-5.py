# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node, key):
            if not node:
                return None

            if key < node.val:
                node.left = dfs(node.left, key)

            elif key > node.val:
                node.right = dfs(node.right, key)

            else:
                # 0 children
                if not node.left and not node.right:
                    return None

                # Only right child
                if not node.left:
                    return node.right

                # Only left child
                if not node.right:
                    return node.left

                # Two children
                successor = node.right

                while successor.left:
                    successor = successor.left

                node.val = successor.val
                node.right = dfs(node.right, successor.val)

            return node

        return dfs(root, key)