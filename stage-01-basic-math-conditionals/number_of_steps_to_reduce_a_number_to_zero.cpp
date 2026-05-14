// Problem: Number of Steps to Reduce a Number to Zero
// Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
// Pattern: Simulation
// Difficulty: Easy
// Date: 2026-05-13

// Approach: Repeatedly reduce the number until it becomes zero.
// If the number is even, divide it by 2; otherwise, subtract 1.
// Count the number of operations performed.
// Time: O(log n) | Space: O(1)

// Local testing with manual input
#include <iostream>
using namespace std;

class Solution {
public:
    int numberOfSteps(int num) {
        
        int steps = 0;
        while (num > 0){
            if (num % 2 == 0){
                num /= 2;
            }else{
                num -=1;
            }
            steps += 1;
        }
        return steps;
    }
};

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    Solution sol;
    int result = sol.numberOfSteps(num);

    cout << "Number of steps: " << result << endl;

    return 0;
}