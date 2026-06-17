# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        #find mid
        slow = head
        fast=head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        prev_node=None
        curr =slow

        while curr:
            next_node=curr.next
            curr.next = prev_node
            prev_node =curr
            curr=next_node
        
        l1=head
        l2=prev_node
        while l1 and l2:
            tmp1 =l1.next  
            tmp2 =l2.next
            l1.next=l2
            if not tmp1:
                break
            l2.next = tmp1
            l1=tmp1
            l2=tmp2

        