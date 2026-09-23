# ======================================
# LeetCode Problem: valid palindrome
# Language: python3
# Link: https://leetcode.com/problems/valid-palindrome/
# Synced by: LinkCode
# Date: 9/23/2026, 1:11:55 PM
# ======================================


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True