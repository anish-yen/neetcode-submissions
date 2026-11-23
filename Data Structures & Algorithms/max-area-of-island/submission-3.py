class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        best = 0

        visited = set()
        def dfs(r, c):
            if r< 0 or c<0 or r>=len(grid) or c>=len(grid[0]): #remember bounds conditions
                return 0 
            if (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))   
            
            return 1 + (     
            + dfs(r+1, c)
            + dfs(r-1, c)
            + dfs(r, c+1)
            + dfs(r, c-1) 
            )

        #loop grid- start dfs when find unvisited
        #if out of bournds, return zero
        #otherwise mark cell as visited
        #add one for each, find best area

        for i in range(len(grid)) :
            for j in range(len(grid[0])):
                if grid[i][j] ==1 and (i,j) not in visited:
                    best = max(best, dfs(i,j))
        return best