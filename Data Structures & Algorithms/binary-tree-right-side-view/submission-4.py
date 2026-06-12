# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        toReturn = []
        q = deque([(root, 0)])
        while q:
            x = q.popleft()
            if x[0] is None:
                return toReturn
            else:
                if x[0].right:
                    q.append((x[0].right, x[1] + 1))
                if x[0].left:
                    q.append((x[0].left, x[1] + 1))
            if x[1] == len(toReturn) - 1:
                continue
            else:
                toReturn.append(x[0].val)
        return toReturn