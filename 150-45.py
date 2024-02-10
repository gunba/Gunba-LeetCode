class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = [float('inf')]
        def findValidJump(x, n, m):
            # If this node is 0 or less, we can't jump?
            if len(n) == 1:
                # Reached last node
                if m[0] > x:
                    m[0] = x
            elif n[0] > 0:
                # Iterate through possible jumps from this position
                for j in reversed(range(1, n[0]+1)):
                    # If jump has an exit point
                    if len(n) > j:
                        findValidJump(x + 1, n[j:], m)
            
        findValidJump(1, nums, m)
        return m[0]
