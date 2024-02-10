class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        repeat = 0
        num = nums[0]
        
        repeat_max = 0
        num_max = num

        for i in range(1, len(nums)):
            if nums[i] == num:
                repeat += 1
                if repeat > repeat_max:
                        repeat_max = repeat
                        num_max = num
            else:
                repeat = 0
                num = nums[i]

        return num_max