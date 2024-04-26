# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        nodes = []
        def processNode(node):
            if node is None:
                return
            else:
                nodes.append(node.val)
                processNode(node.left)
                processNode(node.right)

        processNode(root)
        nodes.sort()

        min_dif = float('inf')
        prev = min_dif

        for x in nodes:
            local_dif = abs(prev-x)
            if local_dif < min_dif:
                min_dif = local_dif
            prev = x

        return min_dif
            

        