# [Missing Number](https://leetcode.com/problems/missing-number/)

## EASY (Tue 31 Jan 2023)

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

I had previously done a similar tutorial question for COMP3121 Wk1. This method ensures efficient time complexity.

# Approach

<!-- Describe your approach to solving the problem. -->

Uses a mathematical approach, the arithmetic sum.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  To get the actual sum: $$O(n)$$

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(1)$$

# Code

```py
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sum = 0
        for num in nums:
            sum += num

        # Get sum of numbers from range formula
        highestNum = len(nums) # Based on assumption only 1 missing number
        expectedSum = highestNum*(highestNum + 1) / 2

        return int(expectedSum - sum)
```
