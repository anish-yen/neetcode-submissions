# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        ptr = head
        left = list1
        right = list2


        if not list1:
            return list2
        if not list2:
            return list1

        while left is not None and right is not None:
            if left.val > right.val:
                ptr.next = right
                right = right.next
            else:
                ptr.next = left
                left = left.next
            ptr = ptr.next
        if left:
            ptr.next = left
        else:
          ptr.next = right
        return head.next