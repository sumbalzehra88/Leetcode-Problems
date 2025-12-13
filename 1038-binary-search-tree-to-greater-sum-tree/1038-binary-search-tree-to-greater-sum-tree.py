# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.summed = 0

        def traverse(node):
            if not node:
                return 

            traverse(node.right)

            self.summed += node.val
            node.val = self.summed

            traverse(node.left)

        traverse(root)

        return root





