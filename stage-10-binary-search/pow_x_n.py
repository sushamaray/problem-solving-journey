# Problem: Pow(x, n)
# Link: https://leetcode.com/problems/powx-n/
# Pattern: Binary Exponentiation
# Difficulty: Medium
# Date: 2026-05-13

# Approach: Use binary exponentiation to compute x raised to the power n
# in logarithmic time. Repeatedly square the base and halve the exponent.
# If the exponent is negative, invert the base and make the exponent positive.
# Time: O(log n) | Space: O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponents
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        # Binary Exponentiation
        while n > 0:
            # If n is odd, multiply current x to result
            if n % 2 == 1:
                result *= x

            # Square the base
            x *= x

            # Divide exponent by 2
            n //= 2

        return result