# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        avg_tpl = []

        def processRoot(root, depth):
            if root:
                if depth == len(avg_tpl):
                    avg_tpl.append([0, 0.0])
                
                avg_tpl[depth][0] += 1
                avg_tpl[depth][1] += root.val

                processRoot(root.left, depth+1)
                processRoot(root.right, depth+1)

        processRoot(root, 0)

        return [tpl[1] / tpl[0] for tpl in avg_tpl]
        
        
