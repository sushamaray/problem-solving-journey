// Problem: Longest Palindromic Substring
// Link: https://leetcode.com/problems/longest-palindromic-substring/
// Pattern: Expand Around Center
// Difficulty: Medium
// Date: 2026-05-13

// Approach: Treat each character (and each gap between two characters)
// as the center of a palindrome. Expand outward while the characters
// on both sides are equal, and keep track of the longest palindrome found.
// Time: O(n^2) | Space: O(1)

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.length() < 2) {
            return s;
        }

        int start = 0;
        int maxLength = 1;

        for (int i = 0; i < s.length(); i++) {
            // Odd-length palindrome (e.g., "aba")
            expand(s, i, i, start, maxLength);

            // Even-length palindrome (e.g., "abba")
            expand(s, i, i + 1, start, maxLength);
        }

        return s.substr(start, maxLength);
    }

private:
    void expand(const string& s, int left, int right,
                int& start, int& maxLength) {
        while (left >= 0 &&
               right < s.length() &&
               s[left] == s[right]) {

            int currentLength = right - left + 1;

            if (currentLength > maxLength) {
                start = left;
                maxLength = currentLength;
            }

            left--;
            right++;
        }
    }
};

// Local testing with manual input
int main() {
    string s;
    cout << "Enter a string: ";
    cin >> s;

    Solution sol;
    string result = sol.longestPalindrome(s);

    cout << "Longest palindromic substring: " << result << endl;

    return 0;
}