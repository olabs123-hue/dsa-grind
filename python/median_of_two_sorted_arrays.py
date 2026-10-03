# ======================================
# LeetCode Problem: median of two sorted arrays
# Language: python3
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Synced by: LinkCode
# Date: 10/3/2026, 1:55:31 PM
# ======================================


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for binary search efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2  # partition point in nums1
            j = half - i             # partition point in nums2
            
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Correct partition found
                if (m + n) % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return max(nums1_left, nums2_left)
            elif nums1_left > nums2_right:
                right = i - 1  # move partition in nums1 left
            else:
                left = i + 1   # move partition in nums1 right