class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parents = [0] * n
        for i in range(len(parents)):
            parents[i] = i

        #[[0,1],[1,2],[3,4]]

        #parent 1 - 0
        #parent 2 - 1 - 0
        count = n
        #parent3-4

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node]) #recursive call change each parent to root node
            return parents[node]

        def union(n1, n2):
            root1 = find(n1)
            root2 = find(n2)

            if root1 == root2:
                return False
            parents[root2] = root1
            return True

        for edge in edges:
            if union(edge[0], edge[1]):
                count -= 1
        return count

        #define find change node-recursive call
        #union find if connected update root decrease count
        #run union on all edges
        #no cycle so no need for dfs hashmap

    """
    from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #build adjacency list
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)  #undirected graph

        visit = set()
        count = 0

        def dfs(node):
            if node in visit:
                return

            visit.add(node)

            for nei in adj[node]:
                dfs(nei)

        #run dfs on every unvisited component
        for i in range(n):
            if i not in visit:
                dfs(i)
                count += 1

        return count
        """