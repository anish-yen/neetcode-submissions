"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {} # map node to clone

        def dfs(node):
            
            if not node:
                return None #edge case?
            
            if node in visited:
                return visited[node] #prevents cycel but return NODE to maintain onnection in graph
                 #need to return node along wiht it. already visited so neighbors share neighbors 
            
            clone = Node()
            clone.val = node.val
            visited[node] = clone #already visited- so n

            for n in node.neighbors:
                clone.neighbors.append( dfs(n))
            return clone #returning starting call clone already returns whole graph because connected components
            
        return dfs(node)