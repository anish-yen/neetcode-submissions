# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        head = ListNode()
        ptr = head
        if l1 == None:
                return list2
        elif l2 == None:
                return list1

        while l1 and l2:
            if l1.val > l2.val:
                ptr.next = l2
                l2 = l2.next
            else:

                ptr.next = l1
                l1 = l1.next
            ptr = ptr.next
        if l1:
            ptr.next = l1
        else:
          ptr.next = l2
        return head.next 
         
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy head
        ptr = dummy

        l1, l2 = list1, list2

        while l1 and l2:
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next

        # Attach the remaining nodes (one of l1 or l2 could be non-empty)
        ptr.next = l1 if l1 else l2

        return dummy.next
"""