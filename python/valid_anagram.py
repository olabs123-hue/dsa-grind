# ======================================
# LeetCode Problem: valid anagram
# Language: python3
# Link: https://leetcode.com/problems/valid-anagram/
# Synced by: LinkCode
# Date: 9/9/2026, 4:10:24 PM
# ======================================


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
