# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        r = head
        l = None

        while r:
            temp = r.next #store temp with right and next
            r.next = l #point right to prev
            l = r #update prev
            r = temp #update r
        
        return l

