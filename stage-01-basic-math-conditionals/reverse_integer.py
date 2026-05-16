# Problem: Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/
# Pattern: Number Reversal
# Difficulty: Medium
# Date: 2026-05-13

# Approach: Extract digits one by one and build the reversed number.
# Before appending each digit, check whether the next operation would
# overflow the 32-bit signed integer range. If overflow would occur,
# return 0.
# Time: O(log n) | Space: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_num = 0

        while x > 0:
            digit = x % 10
            x //= 10

            # Check for overflow before multiplying by 10
            if reversed_num > INT_MAX // 10:
                return 0
            if reversed_num == INT_MAX // 10 and digit > 7:
                return 0

            reversed_num = reversed_num * 10 + digit

        reversed_num *= sign

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0

        return reversed_num


# Local testing with manual input
if __name__ == "__main__":
    x = int(input("Enter an integer: "))

    sol = Solution()
    result = sol.reverse(x)

    print("Reversed integer:", result)