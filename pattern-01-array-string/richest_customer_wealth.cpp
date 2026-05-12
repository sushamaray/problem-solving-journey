// Problem: Richest Customer Wealth
// Link: https://leetcode.com/problems/richest-customer-wealth/
// Pattern: Matrix Traversal
// Difficulty: Easy
// Date: 2026-05-12

// Approach: Traverse each row of the 2D array, calculate the sum of all
// bank balances for each customer, and keep track of the maximum sum found.
// Time: O(m × n) | Space: O(1)

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int maxWealth = 0;
        int rows = accounts.size();
        int columns = accounts[0].size();

        for (int i = 0; i < rows; i++) {
            int wealth = 0;

            for (int j = 0; j < columns; j++) {
                wealth += accounts[i][j];
            }

            maxWealth = max(maxWealth, wealth);
        }

        return maxWealth;
    }
};

// Local testing with manual input
int main() {
    int m, n;

    cout << "Enter number of customers (rows): ";
    cin >> m;

    cout << "Enter number of bank accounts (columns): ";
    cin >> n;

    vector<vector<int>> accounts(m, vector<int>(n));

    cout << "Enter the bank balances for each customer:\n";
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> accounts[i][j];
        }
    }

    Solution sol;
    cout << "Maximum Wealth: "
         << sol.maximumWealth(accounts) << endl;

    return 0;
}