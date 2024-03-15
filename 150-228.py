class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        result = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    result.append(str(start))
                else:
                    result.append("{}->{}".format(start, end))
                start = nums[i]
        
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append("{}->{}".format(start, nums[-1]))
        
        return result