class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        total_water_space = 0
        left = 0
        right = len(height) - 1
        left_max = right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water_space += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water_space += right_max - height[right]
                right -= 1

        return total_water_space

test = Solution()


test.trap([0,1,0,2,1,0,1,3,2,1,2,1])


