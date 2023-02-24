# [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

## MEDIUM (Thursday 23 Feb 2023)

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

### Naive Approach

# Approach

<!-- Describe your approach to solving the problem. -->

### Naive Approach/Bruteforce approach - O(n^3)

Generate all possible substrings

### Sliding window - O(n^2)

Takes n time to go back through the window to find the last occurrence of the repeated character

### Optimised sliding window - O(n)

Uses hashset to keep track of the characters currently in the window. If the character has been repeated, shrink the window until there is no repeated character. I don't think my final solution actually moves the beginning of the window to the point after the character that's been repeated : (

# Complexity

- Time complexity:
    <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  Naive Approach/Bruteforce approach - O(n^3)

  Sliding window - O(n^2)

  Optimised sliding window - O(n)

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(n)$$

# Code

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Bruteforce approach - O(n^3)
        # Generate all possible substrings


        # Sliding window - O(n^2)
        # Takes n time to go back through the window to find the
        # last occurrence of the repeated character


        # Optimised sliding window - O(n)
        # Uses hashset to keep track of the characters currently in the window
        i = 0
        j = 0
        maxLength = 0

        currChars = {}

        while (j < len(s)):

            # If no repeating character, expand the window
            if s[j] not in currChars:
                currChars[s[j]] = 1
                j += 1
            else:
                # Character has been repeated, shrink window until there is no repeated character
                del currChars[s[i]]
                i += 1

            if len(currChars) > maxLength:
                maxLength = len(currChars)


        return maxLength
```
