# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        while len(lists) >1:

            merged = []

            for i in range(0, len(lists),2):

                l1 = lists[i]

                if (i+1) < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
            
                merged.append(self.mergeList(l1, l2))

            lists = merged
        
        return lists[0]
            
    
    def mergeList(self, a, b):
        l = a
        r = b
        dummy = ListNode()
        ptr = dummy

        while l is not None and r is not None:
            if l.val>= r.val:
                ptr.next = r
                r = r.next
            else:
                ptr.next = l
                l = l.next
            ptr = ptr.next
            
        if r:
            ptr.next = r
        if l:
            ptr.next = l
        return dummy.next

            
        