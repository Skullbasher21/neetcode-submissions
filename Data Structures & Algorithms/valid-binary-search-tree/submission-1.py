# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], n: int, x: int) -> bool:
            if root is None:
                return True
            else:
                if root.val <= n or root.val >= x:
                    return False
                return helper(root.left, n, root.val) and helper(root.right, root.val, x)
        return helper(root, float('-inf'), float('inf'))