// Problem: Palindrome Number
// Link: https://leetcode.com/problems/palindrome-number/
// Pattern: Number Reversal
// Difficulty: Easy
// Date: 2026-05-13

// Approach: Reverse only half of the digits and compare it with the
// remaining half. Negative numbers and numbers ending in 0 (except 0)
// cannot be palindromes.
// Time: O(log n) | Space: O(1)

#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        // Negative numbers are not palindromes.
        // Numbers ending with 0 cannot be palindromes unless the number is 0.
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversedHalf = 0;

        // Reverse half of the number
        while (x > reversedHalf) {
            int digit = x % 10;
            reversedHalf = reversedHalf * 10 + digit;
            x /= 10;
        }

        // For even number of digits: x == reversedHalf
        // For odd number of digits: x == reversedHalf / 10
        return x == reversedHalf || x == reversedHalf / 10;
    }
};

// Local testing with manual input
int main() {
    int x;
    cout << "Enter a number: ";
    cin >> x;

    Solution sol;
    bool result = sol.isPalindrome(x);

    cout << "Is palindrome: " << (result ? "true" : "false") << endl;

    return 0;
}