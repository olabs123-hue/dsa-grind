# ======================================
# LeetCode Problem: pascals triangle
# Language: python3
# Link: https://leetcode.com/problems/pascals-triangle/
# Synced by: LinkCode
# Date: 9/16/2026, 8:07:29 AM
# ======================================


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)

        return triangle