class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_indices = {}

        for index, num in enumerate(nums):
            if num in num_indices and index - num_indices[num] <= k:
                return True
            num_indices[num] = index

        return False
