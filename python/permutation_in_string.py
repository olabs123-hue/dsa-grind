# ======================================
# LeetCode Problem: permutation in string
# Language: python3
# Link: https://leetcode.com/problems/permutation-in-string/
# Synced by: LinkCode
# Date: 9/18/2026, 11:55:29 PM
# ======================================


from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])
        
        if s1_count == window_count:
            return True
        
        for i in range(len1, len2):
            # Add the new character entering the window
            window_count[s2[i]] += 1
            
            # Remove the character leaving the window
            left_char = s2[i - len1]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            if window_count == s1_count:
                return True
        
        return False