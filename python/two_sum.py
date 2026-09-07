# ======================================
# LeetCode Problem: two sum
# Language: python3
# Link: https://leetcode.com/problems/two-sum/
# Synced by: LinkCode
# Date: 9/7/2026, 2:30:06 PM
# ======================================


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]