class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        while len(nums) > j:
            if j > 1 and nums[j] == nums[j-2]:
                nums.pop(j)
                j -= 1
            else:
                j += 1

        return len(nums)