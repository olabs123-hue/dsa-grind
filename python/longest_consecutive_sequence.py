# ======================================
# LeetCode Problem: longest consecutive sequence
# Language: python3
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Synced by: LinkCode
# Date: 9/19/2026, 12:07:25 AM
# ======================================


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # Only start counting if this is the start of a sequence
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest