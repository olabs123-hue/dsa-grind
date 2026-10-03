# ======================================
# LeetCode Problem: invalid transactions
# Language: python3
# Link: https://leetcode.com/problems/invalid-transactions/
# Synced by: LinkCode
# Date: 10/3/2026, 1:41:03 PM
# ======================================


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city))
        
        invalid = set()
        
        for i in range(len(parsed)):
            name_i, time_i, amount_i, city_i = parsed[i]
            
            if amount_i > 1000:
                invalid.add(i)
                continue
            
            for j in range(len(parsed)):
                if i == j:
                    continue
                name_j, time_j, amount_j, city_j = parsed[j]
                
                if (name_i == name_j and city_i != city_j 
                        and abs(time_i - time_j) <= 60):
                    invalid.add(i)
                    break
        
        return [transactions[i] for i in invalid]    