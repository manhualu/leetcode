[Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
##  EASY (Sun 8 Jan 2023)
==GAVE UP==

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
My first thoughts was inefficient. It was O(n^2) to have a 'potential' prefix which started as 1 char of the first string, then being 2 char etc.
To confirm the prefix was not only potential, we then had to look through all the other words. 

# Approach
<!-- Describe your approach to solving the problem. -->
I cheated and followed this [video] (https://youtu.be/arrSUHv5qQQ), which would only at run through the length of the first string when the array is sorted alphabetically. I guess it'd be that if they all had the same prefix, they would be sorted so that the first guarantees the longest common prefix. But I am still not 100% sure why the array/how would I have known to sort the input in alphabetically first. 

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
$$O(s)$$ where s is the length of the string first when sorted alphabetically

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(1)$$

# Code
```py
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longestCommonPrefix = ""
        strs.sort()
        
        first = strs[0]
        last = strs[len(strs) - 1]
        
        i = 0
        while (i < len(first)):
            if (first[i] == last[i]):
                longestCommonPrefix += first[i]
            else: 
                break

            i += 1

        
        return longestCommonPrefix
 
```

##  First approach (Thurs 25 Aug 2022)

# Code
```py
class Solution:
    import re

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 1

        firstWord = strs[0]

        # Only 1 word in list
        if len(strs) == 1:
            return strs[0]

        while i < len(firstWord) + 1:
            found = False
            j = 1
            potentialPrefix = firstWord[:i]

            while j < len(strs):
                # Prefix
                if re.match(potentialPrefix, strs[j]):
                    found = True
                else:
                    found = False
                    break

                j += 1

            if not found:
                # Not prefix, most common prefix has been found
                break
            else:
                # Common prefix amongst all words
                prefix = potentialPrefix


            i += 1



        return prefix


```
