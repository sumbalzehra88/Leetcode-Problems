# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        q = [root]
        total = 0

        while q:
            node = q.pop(0)

            if low <= node.val <= high:
                total += node.val

            if node.left and node.val > low:
                q.append(node.left)

            if node.right and node.val < high:
                q.append(node.right)

        return total
