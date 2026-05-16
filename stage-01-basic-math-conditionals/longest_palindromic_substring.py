# Problem: Longest Palindromic Substring
# Link: https://leetcode.com/problems/longest-palindromic-substring/
# Pattern: Expand Around Center
# Difficulty: Medium
# Date: 2026-05-13

# Approach: Treat each character (and each gap between two characters)
# as the center of a palindrome. Expand outward while the characters
# on both sides are equal, and keep track of the longest palindrome found.
# Time: O(n^2) | Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        max_length = 1

        def expand(left: int, right: int) -> None:
            nonlocal start, max_length

            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1

                if current_length > max_length:
                    start = left
                    max_length = current_length

                left -= 1
                right += 1

        for i in range(len(s)):
            # Odd-length palindrome (e.g., "aba")
            expand(i, i)

            # Even-length palindrome (e.g., "abba")
            expand(i, i + 1)

        return s[start:start + max_length]


# Local testing with manual input
if __name__ == "__main__":
    s = input("Enter a string: ")

    sol = Solution()
    result = sol.longestPalindrome(s)

    print("Longest palindromic substring:", result)