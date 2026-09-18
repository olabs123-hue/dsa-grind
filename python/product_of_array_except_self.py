# ======================================
# LeetCode Problem: product of array except self
# Language: python3
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Synced by: LinkCode
# Date: 9/19/2026, 12:04:38 AM
# ======================================


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # Pass 1: prefix products (product of everything to the left of i)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Pass 2: suffix products (product of everything to the right of i)
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer