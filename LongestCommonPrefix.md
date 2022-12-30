
# code

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
