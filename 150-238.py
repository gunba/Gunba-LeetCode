import functools
import operator

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        prev = 1
        for i in range(len(nums)):
            ans.append(prev * functools.reduce(operator.mul, nums[i + 1:], 1))
            prev *= nums[i]
        return ans

test = Solution

print(test.productExceptSelf(test, [1,2,3,4]))
        