# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return
        
        #Split the list in half
        fast = head
        slow = head
        l = head
        
                # ADD: find the middle
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        #break the two halves
        fast = slow.next
        slow.next = None 
        
        prev = None

        #Reverse the second half
        while fast is not None:
            temp = fast.next
            fast.next = prev
            prev = fast 
            fast = temp

        #Merge alternately
        dummy = ListNode()

        l1=head
        l2 = prev
        while l1 and l2:
            tmp1 =l1.next  
            tmp2 =l2.next
            l1.next=l2
            l2.next = tmp1 # if dont have temps i create a cycle
            l1=tmp1
            l2=tmp2

        