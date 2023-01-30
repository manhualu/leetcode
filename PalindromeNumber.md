# [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## EASY (Tue 31 Jan 2023)

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

My first thoughts was to use the tricky Python in-built function that makes a string a list. And the function that reads an array with a reversed iterator.

# Approach

<!-- Describe your approach to solving the problem. -->

There are 2 approaches, as seen below

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  $$O(n)$$

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(n)$$

# Code

## Pythonic Approach

```py
class Solution:
    def isPalindrome(self, x: int) -> bool:

        numsArray = list(str(x))
        return list(reversed(numsArray)) == numsArray

```

## Brute-Force Approach

```py
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Get each digit in the int into a list
        digits = []
        for digit in str(x):
            digits.append(digit)

        # 2 pointers, one iterates from start, the other moves from bottom up
        # Break if the digits being pointed are not the same
        i = 0
        j = len(digits) - 1
        while i < j:
            if (digits[i] != digits[j]):
                return False
            i += 1
            j -= 1

        return True

```
