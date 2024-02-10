class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def findValidJump(n):
            # If this node is 0 or less, we can't jump?
            if len(n) == 1:
                # Reached last node
                return True
            elif n[0] > 0:
                # Iterate through possible jumps from this position
                for j in reversed(range(1, n[0]+1)):
                    # If jump has an exit point
                    if len(n) > j and findValidJump(n[j:]):
                        return True
            else:
                return False
            
        return findValidJump(nums)