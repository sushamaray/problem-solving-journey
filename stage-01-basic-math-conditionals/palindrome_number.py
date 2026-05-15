# Problem: Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Pattern: Number Reversal
# Difficulty: Easy
# Date: 2026-05-13

# Approach: Reverse the digits of the given number and compare the
# reversed number with the original number. Negative numbers are
# not palindromes because of the leading minus sign.
# Time: O(log n) | Space: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num


# Local testing with manual input
if __name__ == "__main__":
    x = int(input("Enter a number: "))

    sol = Solution()
    result = sol.isPalindrome(x)

    print("Is palindrome:", result)
    


'''class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes.
        # Numbers ending with 0 cannot be palindromes unless the number is 0.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse half of the number
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # For even number of digits: x == reversed_half
        # For odd number of digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10


# Local testing with manual input
if __name__ == "__main__":
    x = int(input("Enter a number: "))

    sol = Solution()
    result = sol.isPalindrome(x)

    print("Is palindrome:", result)'''