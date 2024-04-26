class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n

        dp = [2, 3]

        for x in range(4, n+1):
            if x == n:
                return dp[0] + dp[1]
            else:
                dp = [dp[1], dp[0] + dp[1]]
                

