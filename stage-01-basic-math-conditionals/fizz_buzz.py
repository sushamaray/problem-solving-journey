'''Problem: Fizz Buzz
Link: https://leetcode.com/problems/fizz-buzz/
Pattern: Simulation
Difficulty: Easy
Date: 2026-05-13

Approach: Iterate from 1 to n. For each number, check divisibility
by 3 and 5 and append "Fizz", "Buzz", "FizzBuzz", or the number
converted to a string to the result array.
Time: O(n) | Space: O(n)'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for i in range (1, n+1):
            if i % 3 == 0 and i % 5 ==0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        
        return answer
    
# Local testing with manual input
if __name__ == "__main__":
    n = int(input("Enter n: "))
    sol = Solution()
    print(sol.fizzBuzz(n))