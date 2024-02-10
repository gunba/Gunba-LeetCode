class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        while x < len(nums):
            if x == 0:
                x += 1
                continue
            elif x == len(nums):
                break
            elif nums[x] == nums[x-1]:
                del nums[x]
            else:
                x += 1

        return len(nums)