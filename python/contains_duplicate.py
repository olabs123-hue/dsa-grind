# ======================================
# LeetCode Problem: contains duplicate
# Language: python3
# Link: https://leetcode.com/problems/contains-duplicate/
# Synced by: LinkCode
# Date: 9/19/2026, 12:08:26 AM
# ======================================


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num - 1 not in seen if False else num in seen:
                return True
            seen.add(num)
        return False