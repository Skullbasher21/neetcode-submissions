# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        toReturn = []
        def inorder(root: Optional[TreeNode]) -> List[int]:
            if root.left:
                inorder(root.left)
            toReturn.append(root.val)
            if root.right:
                inorder(root.right)
            return toReturn
        x = inorder(root)
        return x[k-1]
            


        