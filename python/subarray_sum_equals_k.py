# ======================================
# LeetCode Problem: subarray sum equals k
# Language: python3
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Synced by: LinkCode
# Date: 10/3/2026, 1:43:16 PM
# ======================================


from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1  # empty prefix sums to 0
        
        for num in nums:
            prefix_sum += num
            
            # If (prefix_sum - k) has been seen before, those subarrays sum to k
            count += sum_freq[prefix_sum - k]
            
            sum_freq[prefix_sum] += 1
        
        return count