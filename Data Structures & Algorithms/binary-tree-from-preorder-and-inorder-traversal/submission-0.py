# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#NOT OPTIMAL!!

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


"""
optimal:

class Solution:
    def buildTree(self, preorder, inorder):

        inorder_idx = {}

        for i in range(len(inorder)):
            inorder_idx[inorder[i]] = i

        preorder_pos = 0

        def dfs(left, right):
            nonlocal preorder_pos

            if left > right:
                return None

            root_val = preorder[preorder_pos]
            preorder_pos += 1

            root = TreeNode(root_val)

            mid = inorder_idx[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)
"""