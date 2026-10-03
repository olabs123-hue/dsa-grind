# ======================================
# LeetCode Problem: word search
# Language: python3
# Link: https://leetcode.com/problems/word-search/
# Synced by: LinkCode
# Date: 10/3/2026, 1:56:28 PM
# ======================================


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, i):
            # i = index into word we're currently trying to match
            if i == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols 
                    or board[r][c] != word[i]):
                return False
            
            # Temporarily mark this cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))
            
            # Backtrack: restore the cell for other paths
            board[r][c] = temp
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False