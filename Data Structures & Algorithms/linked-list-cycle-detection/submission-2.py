# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        slow = ptr
        fast = ptr
        while fast is not None and fast.next is not None:
            ptr = ptr.next
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False