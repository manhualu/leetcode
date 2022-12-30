# [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

## EASY (Wed 28 Dec 2022)

==TRY AGAIN WITH FOLLOW UP==

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

I thought this question was going to be very easy like the leetcode that asks you check if two strings are palindromes. I then thought using a stack, like the question that checks whether brackets are closing, would work. I spent a long time trying to get the stack work, but there was always a few edge cases that would cause it to fail.

# Approach

<!-- Describe your approach to solving the problem. -->

I initially tried to abide by the "Follow up" rules i.e. do it in O(n) time and O(1) space. However, the stack wouldn't even be O(1) space. I then just gave up and realised there was a very simple method which was to just run over the linked list and store each value into an array. Then have 2 pointers, one pointing to the first element and the other pointing to the last element. Have pointer 1 incremented, pointer 2 decremented (closing in) until pointer 1 has surpassed pointer 2 to check whether they are the same.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  To store values in array:
  $$O(n)$$

  To check values are equal in array:
  $$O(n)$$

  Overall: $$O(2n)$$, which is $$O(n)$$

- Space complexity:
  <!-- Add your space complexity here, e.g. $$O(n)$$ -->
  $$O(n)$$

# Code

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Stack approach
        stack = []


        # while (head is not None):

        #     if len(stack) == 0:
        #         stack.append(head.val)
        #     else:
        #         print(f"stack is {stack}")

        #         if head.val == stack[-1]:
        #             print(f"removing {stack[-1]}")
        #             stack.pop()
        #         else:
        #             print(f"adding {head.val}")
        #             stack.append(head.val)

        #     head = head.next



        # print(f"stack is {stack}")

        # return len(stack) == 0

        while head is not None:
            stack.append(head.val)
            head = head.next


        # two pointers
        i = 0
        j = len(stack) - 1
        while i < j:
            if stack[i] != stack[j]:
                return False

            i += 1
            j -= 1

        return True

```
