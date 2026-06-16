# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        prev = head
        ptr = head

        if ptr.next is None:
            return None

        for i in range(n):
            ptr = ptr.next
        while ptr.next is not None:
            ptr = ptr.next
            prev = prev.next
        prev.next = ptr
        ptr.next = None

        return head