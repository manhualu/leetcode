"""
Valid Parentheses
    EASY (Tues 6 Sept 2022)
    https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        possibleLeftBrackets = ["(", "{", "["]
        possibleRightBrackets = [")", "}", "]"]
        '''
        Push all left brackets onto stack with its matching index
        e.g. [0] for "()"
        e.g. [0, 2, 1] for "([]{"
        e.g. [0] for "(])"
        
        If right bracket matches the bracket on the top of stack (peek only at it), pop it off
        Otherwise, return False
        Input string is valid only if stack is empty
        '''
        
        myLeftBrackets = []
        
        for bracket in s:
            if bracket in possibleLeftBrackets:
                # Is a left bracket, push to stack
                myLeftBrackets.append(possibleLeftBrackets.index(bracket))
            
            else:
                # Is a right bracket
                if myLeftBrackets == [] or myLeftBrackets[-1] != possibleRightBrackets.index(bracket):
                    # Input string starts with right bracket 
                    # OR left bracket on top of stack has no matching right bracket 
                    return False
                
                # Found matching right bracket for left bracket on top of stack
                myLeftBrackets.pop()
        
        # Input string is valid only if stack is empty
        return myLeftBrackets == []

