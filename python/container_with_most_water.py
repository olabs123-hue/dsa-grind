# ======================================
# LeetCode Problem: container with most water
# Language: python3
# Link: https://leetcode.com/problems/container-with-most-water/
# Synced by: LinkCode
# Date: 9/22/2026, 10:04:37 PM
# ======================================


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area