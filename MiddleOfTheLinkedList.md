# [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list)

## EASY (Wed 21 Dec 2022)

==GAVE UP==

# Intuition

<!-- Describe your first thoughts on how to solve this problem. -->

Iterative approach. Divide total number of nodes by 2, make x, and then get the xth node in the list. BUT I wanted to do recursive because iterative approach would take $$O(n) + O(n)$$ time.

# Approach

<!-- Describe your approach to solving the problem. -->

Recursive, but ==FAILED== and ==GAVE UP==.

# Complexity

- Time complexity:
  <!-- Add your time complexity here, e.g. $$O(n)$$ -->

  $$O(n)$$

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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Tortoise-hare approach

        # slow pointer always points to the middle node wherever fast pointer points to as last node of list.
        slow = head
        fast = head

        while (fast.next is not None):

            if (fast.next.next is not None):
                # Move the fast pointer ahead by 2 nodes
                fast = fast.next.next
            else:
                # Only 1 more node left, can only move fast node forward 1
                fast = fast.next

            # Move the slow pointer ahead by 1 node
            slow = slow.next

        return slow
```
