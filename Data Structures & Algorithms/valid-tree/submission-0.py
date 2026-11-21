from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        visited = set()
        """
        edgemap = defaultdict(list)

        for edge in edges:
            edgemap[edge[0]].append(edge[1])
        
        print(edgemap)
        """

        adj = [[] for _ in range(n)] #for each index have list of undirected neighbors
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)

        #its undirected so dont need dict append both sides to adj list
        #defaultdict(<class 'list'>, {0: [1], 1: [2, 3, 4], 2: [3]})



        def dfs(node, parent):

            if node in visited:
                return False
            
            visited.add(node)

            for n in adj[node]:
                if n == parent: #skip the undirected part if it points back stulle fine
                    continue

                if not dfs(n, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n #visit every node and no cycle

        #run dfs on every node

