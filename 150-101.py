# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def isMirror(left, right):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        if root is None:
            return True
        return isMirror(root.left, root.right)

