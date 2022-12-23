"""
    Roman to Integer
        EASY (Sat 24 Dec 2022)
    https://leetcode.com/problems/roman-to-integer/
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        i = 0
        sum = 0
        while i < len(s) - 1:            
            if romanToIntDict[s[i]] < romanToIntDict[s[i + 1]]:
                # Subtract only when prev roman char is smaller than latter
                sum += romanToIntDict[s[i + 1]] - romanToIntDict[s[i]]

                # Don't need to add latter number as it was already used in the subtraction
                i += 1
            else: 
                sum += romanToIntDict[s[i]]

            i += 1

        # Last char was not skipped
        if i == len(s) - 1:
            sum += romanToIntDict[s[i]]
        
        return sum


"""
(Thur 25 Aug 2022) Solution
"""
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         romanDict = {
#                         "M":1000,
#                         "CM":900,
#                         "D":500,
#                         "CD":400,
#                         "C":100,
#                         "XC":90,
#                         "L":50,
#                         "XL":40,
#                         "X":10,
#                         "IX":9,
#                         "V":5,
#                         "IV":4,
#                         "I":1
#                     }
#         finalSum = 0
                        
#         i = 0
        
#         while i < len(s):  
#             if i != len(s) - 1:
#                 trial = s[i] + s[i + 1]
                
#                  # Try 2 characters first and if they match anything from dict, add to sum
#                 if trial in romanDict.keys():
#                     finalSum += int(romanDict[trial])
#                     # Increment once more because looked at next char
#                     i += 1
                    
#                 else:
#                     # Try 1 character, add to sum
#                     finalSum += int(romanDict[s[i]])

#             else:
#                 # Try 1 character, add to sum
#                 finalSum += int(romanDict[s[i]])
                    
#             i += 1
        
#         return finalSum