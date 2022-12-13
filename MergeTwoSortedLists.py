"""
    Merge Two Sorted Lists
        EASY (Wed 7 Sept 2022)
    https://leetcode.com/problems/merge-two-sorted-lists
"""

# Recursive Solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None: 
            return list2
        
        if list2 == None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)    
            return list2


# Iterative Solution
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         if list1 == None: 
#             return list2

#         if list2 == None:
#             return list1

#         finalHead = ListNode(None, None)
#         curr = finalHead
        
#         while list1 != None and list2 != None: 
#             if list1.val < list2.val:
#                 curr.next = list1
#                 list1 = list1.next
#             else:
#                 curr.next = list2
#                 list2 = list2.next

#             curr = curr.next
            
#         # For the remaining left, append the other list as is because it is sorted already
#         curr.next = list2 if list1 == None else list1

#         return finalHead.next