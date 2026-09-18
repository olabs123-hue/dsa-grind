# ======================================
# LeetCode Problem: top k frequent elements
# Language: python3
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Synced by: LinkCode
# Date: 9/19/2026, 12:02:59 AM
# ======================================


from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)