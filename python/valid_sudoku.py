# ======================================
# LeetCode Problem: valid sudoku
# Language: python3
# Link: https://leetcode.com/problems/valid-sudoku/
# Synced by: LinkCode
# Date: 9/19/2026, 12:05:47 AM
# ======================================


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                box_idx = (r // 3) * 3 + (c // 3)
                
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        
        return True