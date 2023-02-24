# [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## MEDIUM (Sunday 5 Feb 2023)

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

### Naive Approach

# Approach

<!-- Describe your approach to solving the problem. -->

### Naive Approach

aa

### Kadane's Algorithm (Dynamic Programming)

qq

### Divide and Conquer

qq

# Complexity

- Time complexity:
    <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  Trivial method:
  $$O(nlogn)$$

  Better method:
  $$O(n)$$

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->

  Trivial method:
  $$O(n)$$

  Better method:
  $$O(n)$$

# Code

## Trivial method O(nlogn)

```py
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredArray = []

        for num in nums:
            squaredArray.append(num**2)

        squaredArray.sort()
        # Returns array of the squares of each number in non-decreasing order.
        return squaredArray

```

## O(n) method

```py
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squaredArray = []

        totalSoFar = len(nums) - 1
        i = 0
        j = len(nums) - 1

        # Two pointers
        while totalSoFar >= 0:
            if nums[i]**2 > nums[j]**2:
                # Negative number when squared is bigger, insert to beginning
                squaredArray.insert(0, nums[i]**2)
                i += 1
            else:
                # Positive number when squared is bigger, insert to beginning
                squaredArray.insert(0, nums[j]**2)
                j -= 1

            totalSoFar -= 1

        return squaredArray

```
