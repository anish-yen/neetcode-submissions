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
        #need to have the clones one pass because can point clones to other part so need two pass
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
    """

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dummy = head

        # Pass 1: Create clones directly after originals
        while dummy is not None:
            clone = Node(dummy.val)
            clone.next = dummy.next
            dummy.next = clone
            dummy = clone.next

        # Pass 2: Set random pointers
        dummy = head

        while dummy is not None:
            clone = dummy.next

            if dummy.random is not None:
                clone.random = dummy.random.next
            else:
                clone.random = None

            dummy = clone.next

        # Pass 3: Separate the two lists
        dummy = head
        copyHead = head.next

        while dummy is not None:
            clone = dummy.next
            dummy.next = clone.next

            if clone.next is not None:
                clone.next = clone.next.next

            dummy = dummy.next

        return copyHead
 """