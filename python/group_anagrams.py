# ======================================
# LeetCode Problem: group anagrams
# Language: python3
# Link: https://leetcode.com/problems/group-anagrams/
# Synced by: LinkCode
# Date: 9/19/2026, 12:01:40 AM
# ======================================


from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        
        return list(groups.values())     