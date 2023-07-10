# Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        def dfs(node):
            if not node:
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return values