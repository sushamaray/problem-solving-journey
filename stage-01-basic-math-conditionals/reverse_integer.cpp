// Problem: Reverse Integer
// Link: https://leetcode.com/problems/reverse-integer/
// Pattern: Number Reversal
// Difficulty: Medium
// Date: 2026-05-13

// Approach: Extract digits one by one and build the reversed number.
// Before appending each digit, check whether the next operation would
// overflow the 32-bit signed integer range. If overflow would occur,
// return 0.
// Time: O(log n) | Space: O(1)

#include <iostream>
#include <climits>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        int reversed_num = 0;

        while (x != 0) {
            int digit = x % 10;
            x /= 10;

            // Check for overflow before multiplying by 10
            if (reversed_num > INT_MAX / 10 ||
                (reversed_num == INT_MAX / 10 && digit > 7)) {
                return 0;
            }

            // Check for underflow before multiplying by 10
            if (reversed_num < INT_MIN / 10 ||
                (reversed_num == INT_MIN / 10 && digit < -8)) {
                return 0;
            }

            reversed_num = reversed_num * 10 + digit;
        }

        return reversed_num;
    }
};

// Local testing with manual input
int main() {
    int x;
    cout << "Enter an integer: ";
    cin >> x;

    Solution sol;
    int result = sol.reverse(x);

    cout << "Reversed integer: " << result << endl;

    return 0;
}