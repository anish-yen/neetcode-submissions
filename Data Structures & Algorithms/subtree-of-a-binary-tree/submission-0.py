# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs (node):
            if node is None:
                return False

            if sametree(node, subRoot):
                return True
            else:
                return dfs(node.left) or dfs(node.right) # either side can be fine
        def sametree(root1, root2):
            
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False
            if root1.val  !=root2.val :
                return False
            return sametree(root1.left, root2.left) and sametree(root1.right, root2.right)
            # same tree means both sides must be same
        return dfs(root)