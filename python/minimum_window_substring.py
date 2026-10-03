# ======================================
# LeetCode Problem: minimum window substring
# Language: python3
# Link: https://leetcode.com/problems/minimum-window-substring/
# Synced by: LinkCode
# Date: 10/3/2026, 1:54:58 PM
# ======================================


from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        required = len(need)  # number of unique chars in t that must be satisfied
        
        window = {}
        formed = 0  # number of unique chars currently satisfied in the window
        
        left = 0
        min_len = float('inf')
        min_left = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                formed += 1
            
            # Try to shrink the window from the left while it's still valid
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]