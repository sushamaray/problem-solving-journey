# Problem: Richest Customer Wealth
# Link: https://leetcode.com/problems/richest-customer-wealth/
# Pattern: Matrix Traversal
# Difficulty: Easy
# Date: 2026-05-12

# Approach: Iterate through each row (customer), calculate the sum of all
# account balances, and keep track of the maximum row sum.
# Time: O(m × n) | Space: O(1)

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_row_sum = float('-inf')

        for row in accounts:
            current_row_sum = 0

            for amount in row:
                current_row_sum += amount

            if current_row_sum > max_row_sum:
                max_row_sum = current_row_sum

        return max_row_sum


# Local testing with manual input
if __name__ == "__main__":
    accounts = eval(input("Enter accounts (e.g. [[1,2,3],[3,2,1]]): "))
    sol = Solution()
    print("Maximum Wealth:", sol.maximumWealth(accounts))