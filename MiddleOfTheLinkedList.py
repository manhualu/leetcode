"""
    Middle of the Linked List
        EASY (Wed 21 Dec 2022)
    https://leetcode.com/problems/middle-of-the-linked-list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Tortoise-hare approach

        # Slow pointer always points to the middle node wherever fast pointer points to as last node of list.
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

