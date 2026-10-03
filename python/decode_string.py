# ======================================
# LeetCode Problem: decode string
# Language: python3
# Link: https://leetcode.com/problems/decode-string/
# Synced by: LinkCode
# Date: 10/3/2026, 1:44:08 PM
# ======================================


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_str = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                current_str = prev_str + current_str * num
            else:
                current_str += char
        
        return current_str
        