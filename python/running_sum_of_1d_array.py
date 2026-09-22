# ======================================
# LeetCode Problem: running sum of 1d array
# Language: python3
# Link: https://leetcode.com/problems/running-sum-of-1d-array/
# Synced by: LinkCode
# Date: 9/22/2026, 5:20:59 PM
# ======================================


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums