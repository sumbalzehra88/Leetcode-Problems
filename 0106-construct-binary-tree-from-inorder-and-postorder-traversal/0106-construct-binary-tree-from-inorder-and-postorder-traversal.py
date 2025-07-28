# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        root_index = inorder.index(root_val)

        right_subtree = self.buildTree(inorder[root_index+1:], postorder)
        left_subtree = self.buildTree(inorder[:root_index], postorder)

        root = TreeNode(root_val)
        root.left = left_subtree
        root.right = right_subtree

        return root
