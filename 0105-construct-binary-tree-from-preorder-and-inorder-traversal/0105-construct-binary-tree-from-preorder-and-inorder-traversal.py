# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)
        index = inorder.index(root_val)

        left_subtree = self.buildTree(preorder, inorder[:index])
        right_subtree = self.buildTree(preorder, inorder[index+1:])

        root = TreeNode(root_val)
        root.left = left_subtree
        root.right = right_subtree
        return root

        