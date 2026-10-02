# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTreeRecursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

    def isSameTreeIterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        stack = [(p, q)]
        while stack:
            nodeP, nodeQ = stack.pop()
            if not nodeP and not nodeQ:
                continue

            if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False

            stack.append((nodeP.left, nodeQ.left))
            stack.append((nodeP.right, nodeQ.right))

        return True