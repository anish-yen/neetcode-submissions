# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2
        temp = ListNode()
        new = temp

        if not list1:
            return list2
        if not list2:
            return list1

        while left is not None and right is not None:

            if left.val > right.val: 
                new.next = right
                right = right.next
                
            else:
                new.next = left
                left = left.next
            new = new.next
        
        if right:
            new.next = right
        if left:
            new.next = left
        
        return temp.next