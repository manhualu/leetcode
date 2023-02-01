# [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

## EASY (Thur 2 Feb 2023)

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

First is trivial. Loop through array and add the square of everything to the final array. I then thought to just return the final in that order, but realised that when you square a negative number, it could become bigger than the positive numbers. So I then just thought to sort the final array and return it.

# Approach

<!-- Describe your approach to solving the problem. -->

To avoid needing to sort the array, which will take O(nlogn). I thought to use 2 pointers. As the first half is in decreasing order from left to right when squared and the second half is in increasing order from left to right when squared. The divide between the 'half' being the negatives and positives. So we have 2 pointers and compare the numbers from either pointer. We add to final array from back to front, adding in the bigger number.

This is much easier to understand by drawing it out!

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
