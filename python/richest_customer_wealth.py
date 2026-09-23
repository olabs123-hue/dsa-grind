# ======================================
# LeetCode Problem: richest customer wealth
# Language: python3
# Link: https://leetcode.com/problems/richest-customer-wealth/
# Synced by: LinkCode
# Date: 9/23/2026, 1:17:23 PM
# ======================================


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for row in accounts:
            wealth = sum(row)
            max_wealth = max(max_wealth, wealth)
        return max_wealth