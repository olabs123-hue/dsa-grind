# ======================================
# LeetCode Problem: trapping rain water
# Language: python3
# Link: https://leetcode.com/problems/trapping-rain-water/
# Synced by: LinkCode
# Date: 10/3/2026, 1:51:08 PM
# ======================================


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water