# ======================================
# LeetCode Problem: 3sum
# Language: python3
# Link: https://leetcode.com/problems/3sum/
# Synced by: LinkCode
# Date: 10/3/2026, 1:54:17 PM
# ======================================


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Small optimization: if the smallest possible sum is already > 0, stop
            if nums[i] > 0:
                break
            
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the second and third numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return result