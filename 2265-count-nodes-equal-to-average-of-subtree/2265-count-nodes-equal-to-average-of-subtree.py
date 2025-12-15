# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        def traverse(node):
            if not node:
                return 0,0
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            total = left_sum + right_sum + node.val

            total_count = left_count + right_count + 1
            if total//total_count == node.val:
                self.count += 1

            return total, total_count
        traverse(root)
        return self.count


     