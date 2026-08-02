"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #adjList = []
        clone_map ={}
        #map node to clones
        def dfs(node):
            
            if node in clone_map:
                return clone_map[node]
            clone = Node(node.val)
            clone_map[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
            
            
        if not node:
            return None
        return dfs(node)
            
            

            #curr = 
        