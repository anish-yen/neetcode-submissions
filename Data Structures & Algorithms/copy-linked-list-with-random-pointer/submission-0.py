"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None
        
        #node to clone
        oldToCopy = {}

        dummy = head

        while dummy is not None:

            clone = Node(dummy.val)
            oldToCopy[dummy] = clone
            dummy = dummy.next
        #node: clone
        #key node: clone
        #second pass
        
        dummy = head
        while dummy is not None:
            clone = oldToCopy[dummy]
            if dummy.next is not None:
                clone.next = oldToCopy[dummy.next]
            else:
                clone.next = None
            if dummy.random is not None:
                clone.random = oldToCopy[dummy.random]
            else:
                clone.random = None
            dummy = dummy.next
        if head is not None:
            return oldToCopy[head]
        else:
            return None