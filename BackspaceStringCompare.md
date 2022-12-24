# [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)
##  EASY (Sat 24 Dec 2022)

## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Use an array/stack approach

# Approach
<!-- Describe your approach to solving the problem. -->
Loop through the string by char. If it comes across a '#', delete the most recent char. To reduce repeated code for both string s and t, I created a function

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n)$$

# Code
```py
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.process(s) == self.process(t)

    def process(self, string: str) -> []:
        stringRes = []

        for char in string:

            # Backspace character
            if char == "#":

                # Backspacing an empty text, text will continue empty
                if stringRes != []:
                    stringRes.pop()
            else: 
                stringRes.append(char)

        return stringRes
```